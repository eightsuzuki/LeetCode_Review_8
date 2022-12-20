# n = len(nums)
# time: O(n)
# space: O(n)

from typing import List



class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target not in nums:
            return False       
        
        for i in nums:
            if i == target:
                return True
