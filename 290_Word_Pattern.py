# n = len(s), m= len(set(p))
# time: O(n)
# space: O(m)

from typing import List

class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        wordDict = {}
        words = s.split() 

        if len(p) != len(words): 
            return False
        if len(set(p)) != len(set(words)): 
            return False

        for i in range(len(words)):
            if words[i] not in wordDict: 
                wordDict[words[i]] = p[i]
            elif wordDict[words[i]] != p[i]: 
                return False

        return True