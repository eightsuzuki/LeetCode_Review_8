# n = len(nums)
# time: O(n*n)
# space: O(1)

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        n=len(nums)
        
        for i in range(1,n):
            key=nums[i]
            j=i-1
            while j>=0 and key<nums[j]:
                nums[j+1]=nums[j]
                j-=1
                
            nums[j+1]=key