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
        hmap[None] = None

        itr = head
        while itr:
            hmap[itr].next = hmap[itr.next] # 2nd hmap
            hmap[itr].random = hmap[itr.random] 
            itr = itr.next

        return hmap[head]


