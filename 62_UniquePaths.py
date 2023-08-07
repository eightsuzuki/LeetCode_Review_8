# time: O(m*n)
# space: O(1)

from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            path[0][i] = 1
        for i in range(m):
            path[i][0] = 1

        for r in range(1, m):
            for c in range(1, n):
                path[r][c] = path[r-1][c] + path[r][c-1]

        return path[m-1][n-1]