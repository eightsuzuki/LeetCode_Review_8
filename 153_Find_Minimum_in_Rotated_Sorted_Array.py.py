class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
 
        left = 0
        right = len(nums) - 1
 
        while left <= right:
            mid = (right + left) // 2
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1