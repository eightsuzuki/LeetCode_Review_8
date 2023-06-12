# n = len(letters)
# time: O(logn)
# space: O(1)

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters) - 1
        left = 0
        right = n

        if target >= letters[n] or target < letters[0]:
            return letters[0]

        while left < right:
            mid = (left + right) // 2
                        
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return letters[left]      