# n = len(nums)
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
    
        for i in nums:
            if count < 2 or i != nums[count - 2]:
                nums[count] = i
                count += 1

        return count