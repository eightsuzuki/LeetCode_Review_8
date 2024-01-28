# n = len(citations)
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort( reverse = True )
        
        for i, citation in enumerate(citations):
            if i >= citation:
                return i
        
        return len(citations)