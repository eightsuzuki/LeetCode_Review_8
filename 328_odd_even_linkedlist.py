from typing import Optional


class ListNode:
    def __init__(
            self,
            val: int = 0,
            next: "ListNode" = None
    ):
        self.val = val
        self.next = next


class OddEvenList:
    def separate_odd_even(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = tail = head
        while tail.next:
            tail = tail.next
        
        last = tail
        while cur:
            if cur == last:
                return head
            
            if cur.next == last:
                tail.next = cur.next
                cur.next = cur.next.next
                tail.next.next = None
                return head
            
            tail.next = cur.next
            tail = tail.next
            cur.next = cur.next.next
            tail.next = None
            cur = cur.next
        
        return
