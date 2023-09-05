# time: O(n^2)
# space: O(n)

from typing import List

class Solution:
    def numTrees(self, n: int) -> int:
        """Function to calculate the unique BST number

        Args:
            n(int): an integer which means the node number
        
        Returns:
            int: an integer which means the possible BST number
        
        Process:
            cal_unique_BST_num(2) -> [1, , ] -> [1, 1, 2, 5]
        """
        if type(n) is not int:
            raise TypeError(f'input type should be int but {type(n)}')

        dp = [[] for i in range(n + 1)]
        for i in range(len(dp)):
            if i == 0:
                dp[i] = 1
                continue
            
            cur = 0
            for j in range(1, i + 1):
                left_num = dp[j - 1]
                right_num = dp[i - j]
                cur += left_num * right_num
            dp[i] = cur
        
        return dp[-1]