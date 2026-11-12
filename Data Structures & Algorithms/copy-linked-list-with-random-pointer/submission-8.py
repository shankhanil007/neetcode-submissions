"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        ## working with atleast 1 node
        if head == None:
            return None

        itr = head
        while itr:
            itr.next = Node(itr.val, itr.next)
            itr = itr.next.next

        itr = head
        while itr:
            itr.next.random = itr.random.next if itr.random else None ## IMP to check
            itr = itr.next.next

        itr = head
        new_head = head.next ## IMP 2nd list would be broken. So store it

        while itr:
            nxt = itr.next
            itr.next = itr.next.next
            nxt.next = nxt.next.next if nxt.next else None ## IMP to check
            itr = itr.next

        return new_head