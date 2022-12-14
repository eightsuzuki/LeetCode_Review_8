from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from_num_to_index = dict()
        for i in range(len(nums)):
            if nums[i] in from_num_to_index:
                return [from_num_to_index[nums[i]], i]
            
            from_num_to_index[target-nums[i]] = i