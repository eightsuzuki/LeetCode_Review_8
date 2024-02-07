# n = len(nums)
# time: O(n)
# space: O(n)

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupliSet = {}  

        for i in range(len(nums)):  
            if nums[i] not in dupliSet:
                dupliSet[nums[i]] = i
            else:
                if abs(dupliSet[nums[i]] - i) <= k:
                    return True
                dupliSet[nums[i]] = i

        return False