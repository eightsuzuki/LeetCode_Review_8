# n is the total number of nodes in the binary tree
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        if not root.left and not root.right and targetSum == root.val:
            return [[root.val]]
        
        leftNode = self.pathSum(root.left,targetSum-root.val)
        rightNode = self.pathSum(root.right,targetSum-root.val)
        return [[root.val] + x for x in leftNode+rightNode if x]