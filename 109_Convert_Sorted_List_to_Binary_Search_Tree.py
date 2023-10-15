
# n is the total number of nodes in the binary tree
# time: O(n)
# space: O(n)

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def make(self,A):
        if A:
            m = len(A)//2
            root = TreeNode(A[m])
            root.left  = self.make(A[:m])
            root.right = self.make(A[m+1:])
            return root

    def sortedListToBST(self, head):
        A, n = [], head
        while n:
            A.append(n.val)
            n = n.next
        
        return self.make(A)