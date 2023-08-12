# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n

        a = (1, 2)

        for i in range(3, n+1):
            a = (a[1], a[0]+a[1])

        return a[-1]