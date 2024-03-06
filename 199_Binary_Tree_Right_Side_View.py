# h is the height of the tree, m is the number of the nodes
# time: O(n)
# space: O(h)

from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def solve(root, lvl):
            if root:
                if len(res) == lvl:
                    res.append(root.val)
                solve(root.right, lvl + 1)
                solve(root.lef637. Average of Levels in Binary Treet, lvl + 1)
            return

        res = []
        solve(root, 0)
        return res
