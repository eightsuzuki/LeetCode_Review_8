# m, n = len(obstacleGrid), len(obstacleGrid[0])
# time: O(m*n)
# space: O(n)

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        path = [0 for _ in range(len(obstacleGrid[0]))]
        path[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    path[j] = 0
                elif j>0:
                    path[j]+=path[j-1]
        return path[-1]