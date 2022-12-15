# n2 = len(nums2)
# time: O(n2)
# space: O(0)

from typing import List



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        out = []

        for i in nums2:
            if i in nums1:
                out.append(i)
                nums1.remove(i)

        return out