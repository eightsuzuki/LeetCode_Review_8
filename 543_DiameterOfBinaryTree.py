# n = len(root)
# time: O(n)
# space: O(ｌｏｇｎ)

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 0

        cnt=0
        
        def dfs(root):
            nonlocal cnt
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            cnt = max(cnt,left+right)
            return max(left,right)+1

        dfs(root)
        return cnt
