# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, head: Optional[ListNode]): # function definition
        prev, nxt = None, head
        while head != None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 1. Split the list into two halves
        second = slow.next
        slow.next = None  # Cut the connection to prevent cycles
        
        # 2. Reverse the second half
        second = self.reverse(second)
        first = head

        dummy = ListNode()
        itr = dummy

        while second:
            itr.next = first
            first = first.next
            itr = itr.next

            itr.next = second
            second = second.next
            itr = itr.next
        
        if first:
            itr.next = first
        head = dummy.next
