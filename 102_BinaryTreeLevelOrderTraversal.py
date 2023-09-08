# n is the total number of nodes in the binary tree
# time: O(n)
# space: O(n)

from typing import List

# class TreeNode:
#     def __init__(
#             self, 
#             val: int = 0, 
#             left: Optional["TreeNode"] = None, 
#             right: Optional["TreeNode"] = None
#     ):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q =[]
        ans = []
        if(root == None):
            return ans
        else:
            q.append(root)
            while (len(q)>0):
                n=len(q)
                temp=[]
                while(n>0):
                    r=q.pop(0)
                    temp.append(r.val)
                    if(r.left is not None):
                        q.append(r.left)
                    if(r.right is not None):
                        q.append(r.right)
                    n=n-1
                ans.append(temp)
            return ans       