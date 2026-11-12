# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, new_head, nxt = None, head, head
        while new_head != None:
            nxt = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = nxt
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        end = self.reverse(slow)
        new_head = ListNode()
        copy_head = new_head

        while head != slow:
            new_head.next = head
            head = head.next
            new_head = new_head.next
            new_head.next = end
            end = end.next
            new_head = new_head.next
        
        head = copy_head.next
