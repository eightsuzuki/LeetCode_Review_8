from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        # hash map
        # n = len(nums)
        # time: O(n)
        # space: O(n)

        from_num_to_freq = Counter(nums)
        return max((value, key) for key, value in from_num_to_freq.items())[1]
        """

        """
        # sorting
        # time: O(nlogn)
        # space: O(n)

        nums.sort()
        return nums[len(nums) // 2]
        """

        # Voting algorithm
        # time: O(n)
        # space: O(1)
        count = 0
        candidate_of_majority_element = None
        for num in nums:
            if count == 0:
                candidate_of_majority_element = num
            
            if num == candidate_of_majority_element:
                count += 1
            else:
                count -= 1
        
        return candidate_of_majority_element
        