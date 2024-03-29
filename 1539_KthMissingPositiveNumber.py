# n = len(arr)
# time: O(logn)
# space: O(1)

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2
            miss = arr[mid] - mid - 1
            if k <= miss:
                right = mid
            else:
                 left = mid + 1
        
        return k + left