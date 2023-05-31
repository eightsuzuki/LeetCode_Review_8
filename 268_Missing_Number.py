# n = len(nums)
# time: O(n)
# space: O(0)

from typing import List



class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        if 0 not in nums:
            return 0
        
        if len(nums) not in nums:
            return len(nums)
        
        nums.sort()

        for i in range(len(nums)):
            if nums[i+1] != nums[i] + 1:
                return nums[i]+1