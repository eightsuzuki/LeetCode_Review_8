# n = len(s)
# time: O(n^2)
# space: O(n)

from typing import List

class Solution:
    def partition(self, s):

        def backtrack(start, end, tmp):
            if start == end:
                ans.append(tmp[:])
            for i in range(start, end):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(i+1, end, tmp)
                    tmp.pop()
     
        ans = []
        backtrack(0, len(s), [])
        return ans