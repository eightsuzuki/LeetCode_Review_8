# n = len(arr)
# time: O(logn)
# space: O(1)

from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        
        for i in range(len(arr)):
            dou = arr[i]*2
            n = len(arr) - 1
            left = 0
            right = n

            while left <= right:
                mid = (left + right) // 2
                if arr[mid]==dou and mid!= i:
                    return True
                elif arr[mid]<dou:
                    left += 1
                else:
                    right -= 1
        
        return False           