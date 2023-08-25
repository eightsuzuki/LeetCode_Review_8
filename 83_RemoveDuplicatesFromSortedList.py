# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self,
                 val: int = 0,
                 next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

        
# n = The number of nodes in a given linked list
# time: O(n)
# space: O(1)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head

        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head