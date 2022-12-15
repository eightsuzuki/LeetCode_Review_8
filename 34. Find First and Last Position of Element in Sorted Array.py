# n = len(nums)
# time: O(n)
# space: O(n)

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        output = [-1,-1]
        if not nums: 
            return output
        
        count = 0

        for i in range(len(nums)):
            if nums[i] == target and count == 0:
                output[0] = i
                count = 1
            if nums[i] == target and count == 1:
                output[1] = i
                
        return output
