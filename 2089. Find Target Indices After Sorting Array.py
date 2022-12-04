class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        Out = []
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == target:
                Out.append(i)
                count += 1

        return Out
