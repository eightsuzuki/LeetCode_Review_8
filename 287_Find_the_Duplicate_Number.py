# n = len(nums)
# time: O(n)
# space: O(1)

from typing import List



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        count = {}
        for i in nums:
            if i in count:
                return i
            else:
                count[i] = i
