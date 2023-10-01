# n = len(nums)
# time: O(n)
# space: O(1)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """Function to find a subarray that has the largest product, and
        returns the product.

        Args:
            nums (list[int]): Integer array
                (-10 <= nums[i] <= 10, 1 <= len(nums) <= 2 * 10**4)
        
        Returns:
            int: The largest product.
        
        Raises:
            TypeError
            ValueError
        """
        if type(nums) is not list:
            raise TypeError(f"Type of {nums} is not list.")
    
        if type(nums[0]) is not int:
            raise TypeError(f"{nums} contains an element which is not int.")
        
        NUMS_MIN = -10
        NUMS_MAX = 10
        if nums[0] < NUMS_MIN or nums[0] > NUMS_MAX:
            raise ValueError(
                f"An element of {nums} is not within the range \
                 [{NUMS_MIN}, {NUMS_MAX}]")

        NUMS_LENGTH_MIN = 1
        NUMS_LENGTH_MAX = 2 * 10**4
        if len(nums) < NUMS_LENGTH_MIN or len(nums) > NUMS_LENGTH_MAX:
            raise ValueError(
                f"Length of {nums} is not within the range \
                 [{NUMS_LENGTH_MIN}, {NUMS_LENGTH_MAX}].")
        
        res = max_product = min_product = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
                   
            res = max(res, max_product)
        
        return res
