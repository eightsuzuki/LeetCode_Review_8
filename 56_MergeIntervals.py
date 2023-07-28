# n = len(intervals)
# time: O(nlogn)
# space: O(n)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        for interval in intervals[1:]:
            start, end = interval
            if ans[-1][1] >= start:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append(interval)
        return ans