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

        curr, prev = head, ListNode(0)
        dummy.next = prev.next = head


        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next

            else:
                prev = prev.next
            curr = curr.next

        return dummy.next