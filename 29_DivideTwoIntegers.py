# time: O(1)
# space: O(1)

from typing import List

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = int(dividend / divisor)
        if n > (2**31 - 1) or n < (-2**31 - 1):
            return 2**31-1
        else:
            return n