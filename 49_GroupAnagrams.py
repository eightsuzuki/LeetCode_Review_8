# n = len(strs)
# time: O(n)
# space: O(n)

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            sortedStr = "".join(sorted(s))

            if sortedStr in ans:
                ans[sortedStr].append(s)
            else:
                ans[sortedStr] = [s]


        return list(ans.values())