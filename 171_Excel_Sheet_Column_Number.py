# n = len(columnTitle)
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        colNum = 0
        j = 0

        for i in range(len(columnTitle), 0, -1) :
            colNum += (ord(columnTitle[i-1]) - 64) * 26**j
            j += 1
        return colNum
        