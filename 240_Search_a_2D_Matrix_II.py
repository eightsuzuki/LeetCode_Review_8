# n = len(nums)
# time: O(n)
# space: O(n)

from typing import List



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            left = 0
            right = len(matrix[0]) - 1
            while left <= right:
                mid = (right + left) // 2
                if target == matrix[i][mid]:
                    return True
                elif target > matrix[i][mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return False
