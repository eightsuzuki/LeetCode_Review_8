class Solution(object):
    def search(self, nums, target):
        count = -1
        
        for i in nums:
            count += 1
            if i == target:
                return count

        if target not in nums:
            return -1
