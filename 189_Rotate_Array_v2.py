
# n = len(nums)
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == k: return

        k = k % n 
        # for i in range(k):
        #     lastNum = nums.pop()
        #     nums.insert(0, lastNum)
        if k != 0:
            nums[:] = nums[-k:]+nums[:n-k]
            
        