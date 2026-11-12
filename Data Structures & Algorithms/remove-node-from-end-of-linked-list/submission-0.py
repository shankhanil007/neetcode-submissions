# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, nxt = None, None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev, nxt, count = None, None, 1
        head = self.reverse(head)
        copy_head = head
        
        if n == 1:
            head = head.next
            return self.reverse(head)
            
        while head:
            nxt = head.next
            if count == n:
                prev.next = nxt
            prev = head
            head = nxt
            count += 1
        return self.reverse(copy_head)

