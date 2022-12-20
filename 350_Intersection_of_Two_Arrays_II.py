# n1 = len(nums1), n2 = len(nums2)
# time: O(n1+n2)
# space: O(n1+n2)

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        a, b = map(Counter, (nums1, nums2)
        return list((a & b).elements())
