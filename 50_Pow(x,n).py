# time: O(log n)
# space: O(1)

from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
                
        if n == 0:
            return 1 if x!=0 else None
        
        if n < 0:
            n = -n
            x = 1/x

        res = 1
        y = x
        while n:
            if n%2:
                res *= y
            n >>= 1
            y *= y
        return res 