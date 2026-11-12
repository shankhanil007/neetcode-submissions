"""
# Definition for a Node.
import itertools
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
            
        itr = head
        while itr:
            itr.next = Node(itr.val, itr.next)
            itr = itr.next.next

        itr = head
        while itr:
            itr.next.random = itr.random.next if itr.random else None
            itr = itr.next.next

        itr = head
        new_head = itr.next

        while itr:
            nxt = itr.next
            itr.next = nxt.next
            nxt.next = nxt.next.next if nxt.next else None
            itr = itr.next

        return new_head
            