# n is the number of the nodes
# time: O(n)
# space: O(log(n))

from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque()
        if root is None:
            return res
        
        q.append(root)

        while q:
            s = len(q)
            r = 0 
            for i in range(s):
                n = q.pop()
                r += n.val
                if n.left: q.appendleft(n.left)
                if n.right: q.appendleft(n.right)
            res.append(r/s)
        
        return res
