# n = len(nums)
# time: O(log n)
# space: O(1)

from typing import List



class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right = len(nums) - 1      
        left = 0
        
        if target not in nums:
            return -1

        while right >= left:
            mid = (right+left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
