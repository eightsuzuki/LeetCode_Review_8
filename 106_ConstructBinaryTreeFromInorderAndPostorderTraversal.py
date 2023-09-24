# n is the total number of nodes in the binary tree
# time: O(n)
# space: O(n)

from collections import deque
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """Function to build binary trees
        Args:
            inorder (List[int]): a list of integer which means preorder traversal of target binary tree
            postorder (List[int]): a list of integer which means inorder traversal of target binary tree
        
        Returns:
            Optional[TreeNode]: target binary tree
        """
        if not inorder or not postorder:
            return None

        root　=　TreeNode(postorder[-1])
        index　=　inorder.index(postorder[-1])
        root.left　=　self.buildTree(inorder[:index],postorder[:index])
        root.right　=　self.buildTree(inorder[index+1:],postorder[index:-1])

        return root
            