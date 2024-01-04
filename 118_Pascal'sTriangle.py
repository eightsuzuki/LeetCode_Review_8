# n = numRows
# time: O(n^2)
# space: O(n^2)

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        if numRows == 0:
            return ans

        ans.append([1])

        for i in range(1, numRows):
            preRow = ans[i - 1]
            curRow = [1]

            for j in range(1, i):
                curRow.append(preRow[j - 1] + preRow[j])

            curRow.append(1)
            ans.append(curRow)

        return ans