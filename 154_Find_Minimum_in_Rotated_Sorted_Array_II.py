# n = len(nums)
# time: O(n)
# space: O(n)

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
 
        left = 0
        right = len(nums) - 1
 
        while left < right:
            mid = (right + left) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
