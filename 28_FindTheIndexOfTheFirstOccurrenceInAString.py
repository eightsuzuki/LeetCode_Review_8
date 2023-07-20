# n = len(needle), m = len(haystack) 
# time: O((m - n) * n)
# space: O(1)

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for a in range(len(haystack)):
                if haystack[a:len(needle)+a] == needle:
                    return a

        else:
            return -1