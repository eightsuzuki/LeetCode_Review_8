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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = [(root, 0)]

        while queue:
            cur, level = queue.pop()
            if cur.left:
                queue.insert(0, (cur.left, level + 1))
            if cur.right:
                queue.insert(0, (cur.right, level + 1))

            if len(ans) <= level:
                ans.append([])

            ans[level].append(cur.val) 

        return ans[::-1]