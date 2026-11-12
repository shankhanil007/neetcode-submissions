# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slowPtr = head
        fastPtr = head

        while fastPtr != None:
            slowPtr = slowPtr.next
            if fastPtr.next == None:
                return False
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                return True
        
        return False
        