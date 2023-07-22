# n = len(candidates)
# time: O(2^n)
# space: O(n)

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def traverse(candid, arr,sm):                   
            if sm == target: self.ans.append(arr)       
            if sm >= target: return                    
            for i in range(len(candid)):               
                traverse(candid[i:], arr + [candid[i]], sm+candid[i])   
        
        self.ans = []                                   
        traverse(candidates,[], 0)
        return self.ans