class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return False       
        
        for i in nums:
            if i == target:
                return True
