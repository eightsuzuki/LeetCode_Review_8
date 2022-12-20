# n = len(nums)
# time: O(nlog n)
# space: O(n)

from typing import List



class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()
        Out = []
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == target:
                Out.append(i)
                count += 1

        return Out
