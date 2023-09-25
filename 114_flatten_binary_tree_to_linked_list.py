from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: Optional["TreeNode"] = None,
            right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class FlattenBinaryTree:
    def flatten_binary_tree(self, root: Optional[TreeNode]) -> TreeNode:
        if not root:
            raise ValueError(f'input is None')
        
        stack = deque()
        if root.right:
            stack.append(root.right)
        
        if root.left:
            stack.append(root.left)
        
        prev = root
        while stack:
            cur = stack.pop()
            prev.left = None
            prev.right = cur
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            prev = cur
        
        return root
