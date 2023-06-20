# n = len(s)
# m = sの異なる文字の数
# time: O(n)
# space: O(min(n*m))

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 
        count = 0
        visited = set()

        for i in range(len(s)):
            if not i == 0:
                visited.remove(s[i-1])
            
            while count < len(s) and s[count] not in visited:
                visited.add(s[count])
                count += 1
            
            ans = max(ans, count - i)
        
        return ans
