# n = len(num)
# time: O(n!)
# space: O(n!)

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs (nums, ans, path):
            if len(nums) == 0:
                ans.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i]==nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:], ans, path+[nums[i]])

        ans = []
        nums.sort()
        dfs(nums, ans, [])
        return ans