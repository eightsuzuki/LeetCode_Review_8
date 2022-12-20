# n = len(nums)
# time: O(log n)
# space: O(1)

from typing import List



class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1
        
        while right > left:
            mid = (left + right) // 2
            
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        
        if nums[right] > nums[mid] :
            return  right
