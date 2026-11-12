# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        copy_node = dummy
        carry = 0

        while l1 and l2:
            result = l1.val + l2.val + carry
            unit = result % 10
            carry = result // 10
            copy_node.next = ListNode(unit)
            copy_node = copy_node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            result = l1.val + carry
            unit = result % 10
            carry = result // 10
            copy_node.next = ListNode(unit)
            copy_node = copy_node.next
            l1 = l1.next

        while l2:
            result = l2.val + carry
            unit = result % 10
            carry = result // 10
            copy_node.next = ListNode(unit)
            copy_node = copy_node.next
            l2 = l2.next

        if carry:
            copy_node.next = ListNode(carry)

        return dummy.next