"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def getOrAddInHmap(self, hmap, key):
        if key in hmap.keys():
            return hmap[key]
        hmap[key] = Node(key.val)
        return hmap[key]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hmap = defaultdict(Node)
        hmap[None] = None
        itr = head

        while itr:
            hmap[itr] = self.getOrAddInHmap(hmap, itr)
            hmap[itr].next = self.getOrAddInHmap(hmap, itr.next)
            hmap[itr].random = self.getOrAddInHmap(hmap, itr.random) 
            itr = itr.next

        return hmap[head]


