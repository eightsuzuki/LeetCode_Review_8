# n = len(num)
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        fast = 0

        for i in range(len(nums) - 1):
            fast = max(fast, i + nums[i])
            if fast >= len(nums) - 1:
                ans += 1
                break
            if i == end:     
                ans += 1    
                end = fast  

        return ans