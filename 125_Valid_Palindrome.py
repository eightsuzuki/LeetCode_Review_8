# n = len(s)
# time: O(n)
# space: O(n)

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def remove_non_alphanumeric_and_lower(input_string):
            cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
            return cleaned_string
        
        s = remove_non_alphanumeric_and_lower(s)
        
        return s == s[::-1]
