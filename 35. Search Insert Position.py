# n = len(nums)
# time: O(n)
# space: O(n)

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if nums[len(nums)-1] < target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
