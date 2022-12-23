# n = len(nums)
# time: O(log(n))
# space: O(1)

from typing import List



class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x

        while left <= right:
            mid = (left+right) // 2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif x < mid**2:
                right = mid - 1
            else:
                left = mid + 1
