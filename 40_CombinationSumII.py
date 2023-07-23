# n = len(candidates)
# time: O(2^n)
# space: O(n)

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, curr, target):
            if not target:
                res.append(curr)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                backtrack(i+1, curr+[candidates[i]], target - candidates[i])
        
        candidates.sort()
        res = []
        backtrack(0, [], target)
        return res