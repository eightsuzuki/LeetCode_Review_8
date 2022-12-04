class Solution(object):
    def searchInsert(self, nums, target):

        if nums[len(nums)-1] < target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
