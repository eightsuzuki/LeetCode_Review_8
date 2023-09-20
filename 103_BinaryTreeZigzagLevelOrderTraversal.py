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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque()
        if root:
            q.append(root)
        level = 1
        while q:
            level_len = len(q)
            level_nodes = []
            for _ in range(level_len):
                node = q.popleft()
                level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level % 2 == 0:
                level_nodes.reverse()
            result.append(level_nodes)
            level += 1
        return result