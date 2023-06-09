# n = headのリンク数
# time: O(n)
# space: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:	
        if not head or not head.next:
            return True
        
        number = []
        s = head

        while s != None:
            number.append(s.val)
            s = s.next

        return number == number[::-1]
