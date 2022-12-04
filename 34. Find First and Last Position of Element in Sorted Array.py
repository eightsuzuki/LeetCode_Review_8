class Solution(object):
    def searchRange(self, nums, target):

        output = [-1,-1]
        if not nums: 
            return output

        for i in range(len(nums)):
            if nums[i] == target:
                output[0] = i
                break

        for i in range(len(nums)):
            if nums[i] == target:
                output[1] = i
                
        return output
