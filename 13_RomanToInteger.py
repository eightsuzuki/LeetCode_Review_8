# n = len(s)
# time: O(n)
# space; O(1)

from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        rNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0

        for i in range(len(s) - 1):
            if rNum[s[i]] < rNum[s[(i + 1)]]:
                number -= rNum[s[i]]
            else:
                number += rNum[s[i]]

        return number + rNum[s[-1]]
