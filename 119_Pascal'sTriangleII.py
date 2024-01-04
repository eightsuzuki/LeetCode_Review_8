# n = rowIndex
# time: O(n)
# space: O(n)

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        preRow = 1
  
        for i in range(1, rowIndex + 1):
            nextVal = preRow * (rowIndex - i + 1) // i
            ans.append(nextVal)
            preRow = nextVal
        return ans