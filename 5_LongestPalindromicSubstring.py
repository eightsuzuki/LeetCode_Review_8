# n = len(s)
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def check(i, j):
            left = i
            right = j - 1
            
            while left < right:
                if s[left] != s[right]:
                    return False        
                left += 1
                right -= 1
            return True
        
        start = 0
        length = len(s)
        
        while length > 0:
            for i in range(len(s) - length + 1):
                if check(i, i + length):
                    return s[i:i + length]
            length -= 1

        return ""
    