# n = len(n)
# time: O(n^2)
# space: O(n^2)

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        matrix[0][0] = 1

        if n==1:
            return matrix
        
        r,c,dr,dc = 0,0,0,1

        for current in range(1, n*n+1) :
            matrix[r][c] = current

            if not (0<= r+dr < n and 0<=c+dc<n and matrix[r+dr][c+dc] == 0 ) :

                dr, dc = dc, -dr
            
            r += dr
            c += dc
        
        return matrix
