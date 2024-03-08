# n is the number of the nodes, h is the hight of the tree
# time: O(n)
# space: O(n)

from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.inorder(root, arr)  
        return arr == list(sorted(set(arr)))  

    def inorder(self, root, arr):
        if root is not None:  
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)
