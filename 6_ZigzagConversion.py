# n = len(s)
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        i = 0
        direction = -1

        for word in s:
            rows[i] += word
            if i == 0 or i == numRows - 1:
                direction *= -1
            i += direction
            
        return ''.join(rows)

