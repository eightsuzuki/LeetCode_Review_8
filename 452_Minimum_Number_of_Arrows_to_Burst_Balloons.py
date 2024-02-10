# n = len(points)
# time: O(nlogn)
# space: O(1)

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])     
        tally = 1
        bow = points[0][1]
                                      
        for start, end in points:              
            if bow < start:                
                bow = end                   
                tally += 1                   
                                             
        return tally                       