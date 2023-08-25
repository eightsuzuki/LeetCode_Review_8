from typing import Optional

# Definition for singly-linked list.
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_head, right_head = ListNode(), ListNode()
        left, right = left_head, right_head
        
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        
        left.next = right_head.next
        right.next = None
        
        return left_head.next