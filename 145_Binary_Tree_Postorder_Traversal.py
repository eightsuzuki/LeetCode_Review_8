# n is the number of nodes
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        postorder, stack = [], [root]
        while stack:
            node = stack.pop()
            if not node: 
                continue
            postorder.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return postorder[::-1]