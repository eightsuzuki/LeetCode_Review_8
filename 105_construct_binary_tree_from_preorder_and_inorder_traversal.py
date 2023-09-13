from collections import deque
from typing import Optional, List


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


class BinaryTreeConstructer:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Function to build binary trees
        Args:
            preorder (List[int]): a list of integer which means preorder traversal of target binary tree
            inorder (List[int]): a list of integer which means inorder traversal of target binary tree
        
        Returns:
            Optional[TreeNode]: target binary tree
        """
        """if type(preorder) is not list:
            raise TypeError(f'input type should be list, but {type(preorder)}')
        
        if not preorder and not inorder:
            return

        if type(preorder[0]) is not int:
            raise TypeError(f'input type should be list of int, but list of {type(preorder[0])}')
        
        if len(preorder) != len(inorder):
            raise ValueError()
        """
        if not preorder:
            return None

        node = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        node.left = self.build_tree(preorder[1: 1 + idx], inorder[0: idx])
        node.right = self.build_tree(preorder[1 + idx:], inorder[idx + 1:])
        return node
            