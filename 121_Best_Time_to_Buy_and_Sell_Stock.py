# n = len(prices)
# time: O(n)
# space: O(1)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPurchase = prices[0]

        for i in range(0, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        
        return maxProfit