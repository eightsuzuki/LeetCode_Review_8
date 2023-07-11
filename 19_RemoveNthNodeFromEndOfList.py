# n = len(head)
# time: O(n)
# space: O(1)

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        if head.next==None and n==1: return None
        if n==1:
            c=head
            while c.next.next:
                c=c.next
            c.next=None
            return head

        currentnode=head
        for x in range(n):

            currentnode=currentnode.next
            if currentnode==None and x+1==n:
                return head.next

        p1=head
        
        while currentnode.next:
            currentnode=currentnode.next
            p1=p1.next
            
       
        p1.next=p1.next.next
        return head
