# n = len(intervals)
# time: O(nlogn)
# space: O(n)

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        intervals.sort()

        if len(intervals) == 0:
            return [newInterval]

        intervals.append([math.inf, -math.inf])

        for index, (start, end) in enumerate(intervals):
            if newInterval[1] < start:
                return ans + [newInterval] + intervals[index:-1]
            elif end < newInterval[0]:
                ans.append([start, end])
            else:
                newInterval = [
                    min(newInterval[0], start), max(newInterval[1], end)
                ]

        return ans