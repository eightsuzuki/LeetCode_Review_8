# n = len(nums)
# time: O(log n)
# space: O(1)

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:


        count = 0
        col_num = len(grid[0])
        
        for col in grid:
            left = 0
            right = len(col) - 1
            
            while left <= right:
                mid = (right+left) // 2
                if col[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1

            count += col_num - left

        return count

