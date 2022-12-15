# n = len(nums)
# time: O(n)
# space: O(n)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target not in nums:
            return -1

        array_count = -1
        
        for i in nums:
            array_count += 1
            if i == target:
                return array_count
