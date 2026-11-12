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
        
        hmap = defaultdict(Node)
        itr = head

        while itr:
            hmap[itr] = Node(itr.val)
            itr = itr.next

        itr = head
        while itr:
            hmap[itr].next = hmap[itr.next] if itr.next else None
            hmap[itr].random = hmap[itr.random] if itr.random else None
            itr = itr.next

        return hmap[head] if head else None


