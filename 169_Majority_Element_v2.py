# n = len(nums), m = len(set(nums))
# time: O(n)
# space: O(m)

from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        n = len(nums)
        for i in nums:
            dic[i] += 1
            if dic[i] > n/2:
                return i