# n = len(nums)
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

            if sum > ans:
                ans = sum
            
            if sum < 0:
                sum = 0

        return ans