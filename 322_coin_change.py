# n is the value of amount
# time: O(n)
# space:O(n)


from collections import deque
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        queue = deque([(0, 0)])
        visited = {0}
        while queue:
            width = len(queue)
            for _ in range(width):
                node, step = queue.popleft()
                for coin in coins:
                    if node + coin in visited:
                        continue

                    if node + coin == amount:
                        return step + 1

                    elif node + coin < amount:
                        queue.append([node + coin, step + 1])
                        visited.add(node + coin)

        return -1
