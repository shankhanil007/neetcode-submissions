"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    # def getOrAddInHmap(self, hmap, key):
    #     if key in hmap.keys():
    #         return hmap[key]
    #     hmap[key] = Node(key.val)
    #     return hmap[key]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # hmap = defaultdict(Node)
        # hmap[None] = None       ## IMP 
        # itr = head

        # while itr:
        #     hmap[itr] = self.getOrAddInHmap(hmap, itr)
        #     hmap[itr].next = self.getOrAddInHmap(hmap, itr.next)
        #     hmap[itr].random = self.getOrAddInHmap(hmap, itr.random) 
        #     itr = itr.next

        # return hmap[head]

        if head is None:
            return None

        itr = head
        while itr:
            itr.next = Node(itr.val, itr.next)
            itr = itr.next.next

        itr = head
        while itr:
            itr.next.random = itr.random.next if itr.random else None # if check imp
            itr = itr.next.next
        
        newHead = head.next
        itr = head
        while itr:
            copy = itr.next
            itr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            itr = itr.next
        
        return newHead


