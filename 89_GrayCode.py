# n = len(s)
# time: O(n * 2^n)
# space: O(n)

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        s = [0]

        for i in range(n):
            ns=[]
            for j in s:
                ns.append(j + (1<<i))
            s = s + ns[:: -1]
            
        return s