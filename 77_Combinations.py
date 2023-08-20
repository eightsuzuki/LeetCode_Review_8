# time: O(C(n, k))
# space: O(k)

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            if len(path) == k:
                res.append(path[:])
                return

            for j in range(i, n):
                if n-j < k - len(path):
                    return
                path.append(j+1)
                dfs(j+1)
                path.pop()
            
        dfs(0)
        return res