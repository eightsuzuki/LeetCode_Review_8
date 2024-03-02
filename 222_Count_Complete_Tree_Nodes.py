# n is the height of the tree
# time: O(log^2 n)
# space: O(1)

from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = å
        r = root
        heightL = 0
        heightR = 0

        while l:
            heightL += 1
            l = l.left

        while r:
            heightR += 1
            r = r.right

        if heightL == heightR:
            return pow(2, heightL) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)