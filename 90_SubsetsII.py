# n = len(nums)
# time: O(2^n)
# space: O(2^n)

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            for i in range(len(ans)):
                x = ans[i][:]
                x.append(num)
                x.sort()
                if x not in ans:
                    ans.append(x)
        
        return ans

