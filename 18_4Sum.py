# n = len(nums)
# time: O(n**3)
# space: O(n**2)

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twosum(nums, target):
            ans = []
            l, r = 0, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum < target or (l > 0 and nums[l] == nums[l-1]):
                    l += 1
                elif curr_sum > target or (r < len(nums) - 1 and nums[r] == nums[r+1]):
                    r -= 1
                else:
                    ans.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return ans

        def ksum(nums, target, k):
            ans = []
            if not nums:
                return ans
            
            avg_val = target / k
            if avg_val < nums[0] or avg_val > nums[-1]:
                return ans
            
            if k == 2:
                return twosum(nums, target)
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                for subset in ksum(nums[i+1:], target - nums[i], k - 1):
                    ans.append([nums[i]] + subset)
            return ans
        
        nums.sort()
        return ksum(nums, target, 4)