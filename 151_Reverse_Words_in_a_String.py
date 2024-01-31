# n = len(s)
# time: O(n)
# space: O(n)

from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        words = words[::-1]
    
        return ' '.join(words)