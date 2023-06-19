# n = len(s[1]) + len(s[2]) + len(s[3]) ...  
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        
        prefix = strs[0]

        for string in strs:

            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                
                if not prefix:
                    return ""

        return prefix