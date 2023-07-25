# n = len(num)
# time: O(n^2)
# space: O(n^2)

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ans = [tuple(i) for i in matrix]
        for i in range(n):
            for j in range(n):
                matrix[j][n-1-i] = ans[i][j]
