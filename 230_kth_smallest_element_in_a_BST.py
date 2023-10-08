from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: Optional["TreeNode"] = None,
            right: Optional["TreeNode"] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class SmallestTree:
    def kth_smallest_node(self, root: Optional[TreeNode], k: int) -> int:
        # n: node nums
        # time: O(n)
        # space: O(n)
        stack = deque()
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            
            else:
                cur = stack.pop()
                k -= 1
                if not k:
                    return cur.val
                cur = cur.right
        
        raise ValueError(f'the node nums is smaller than k: {k}')