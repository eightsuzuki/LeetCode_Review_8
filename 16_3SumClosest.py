# n = len(nums)  
# time: O(n*n)
# space: O(1)

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        dif = float('inf')
        for i in range(len(nums)-1):
            l, r = i + 1, len(nums) - 1
            while l < r:
                Sum = nums[i] + nums[l] + nums[r]
                if Sum == target:
                    return target
                elif abs(target - Sum) < dif:
                    dif = abs(target - Sum)
                    ans = Sum
                
                if Sum > target:
                    r -= 1
                else:
                    l += 1
        return ans