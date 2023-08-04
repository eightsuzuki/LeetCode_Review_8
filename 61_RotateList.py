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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
                
        if not head:
            return None
        if not head.next:
            return head
        
        old = head
        n = 1
        while old.next:
            old = old.next
            n += 1
        old.next = head

        new = head
        for i in range(n - k % n - 1):
            new = new.next
        newhead = new.next

        new.next = None

        return newhead