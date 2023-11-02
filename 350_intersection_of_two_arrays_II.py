# n = len(set(nums1)) + len(set(nums2))
# time: O(n)
# space: 0(n)
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = map(Counter, (nums1, nums2))
        return list((a & b).elements())


"""
# time: O(nlog n)
# space: O(1)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_len = len(nums1)
        n2_len = len(nums2)
        if n2_len < n1_len:
            n1_len, n2_len = n2_len, n1_len
            nums1, nums2 = nums2, nums1
        nums1.sort()
        nums2.sort()
        res = []
        for num1 in nums1:
            for i, num2 in enumerate(nums2):
                if num1 == num2:
                    res.append(num1)
                    nums2 = nums2[i+1:]
                    break
                elif num1 < num2:
                    nums2 = nums2[i:]
                    break
        return res
"""