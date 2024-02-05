# n = len(s), m = len(t)
# time: O(n+m)
# space: O(n+m)

from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}

        for i in range(len(s)):
            if s[i] not in dict and t[i] not in dict.values():
                dict[s[i]] = t[i]

        string = ""

        for i in range(len(s)):
            if s[i] in dict:
                string += dict[s[i]]
        
        if string == t:
            return True
        return False