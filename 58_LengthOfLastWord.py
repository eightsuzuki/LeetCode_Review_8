# n = len(s)
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        while s and s[-1] == " ":
            s = s[:-1]

        while s and s[-1] != " ":
            s = s[:-1]
            count += 1

        return count