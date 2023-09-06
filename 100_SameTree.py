# n is the number of nodes in the tree with more nodes
# time: O(n)
# space: O(n)

from typing import List

class TreeNode:
    def __init__(
            self, 
            val: int = 0, 
            left: Optional["TreeNode"] = None, 
            right: Optional["TreeNode"] = None
    ):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Function to compare two trees.
        Args:
            p (Optional[TreeNode]): a tree node
            q (Optional[TreeNode]): a tree node
        Returns:
            bool: True if p and q are same trees, False otherwise
        """
        if not p and not q:
            return True

        elif not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
