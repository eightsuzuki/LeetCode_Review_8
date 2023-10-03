# V: the number of node
# time: O(V)
# space: O(V)


from collections import deque
from typing import Optional


class NextNodeNotFoundExeptions(Exception):
    """Raised when there is no node on the right side."""
    pass


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None
    ):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode] = None):
        self.stack = deque()
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """Function to get next node.

        Returns:
            int: The next node value
        Raises:
            GreenBuildNotFoundException: An error when there is no node on the right side.
        """
        if not self.stack:
            raise NextNodeNotFoundExeptions("There is no node on the right side.")

        current_node = self.stack.pop()
        next_root = current_node.right
        while next_root:
            self.stack.append(next_root)
            next_root = next_root.left

        return current_node.val

    def has_next(self) -> bool:
        """Function to check if the next node exists.

        Returns:
            bool: True if there is a next node, False otherwise
        """
        return len(self.stack) >= 1
