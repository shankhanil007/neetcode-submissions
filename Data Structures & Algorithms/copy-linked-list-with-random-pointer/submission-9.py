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
        # hmap[None] = None                         ## IMP to None in Hmap
        # itr = head

        # while itr:
        #     hmap[itr] = self.getOrAddInHmap(hmap, itr)
        #     hmap[itr].next = self.getOrAddInHmap(hmap, itr.next)
        #     hmap[itr].random = self.getOrAddInHmap(hmap, itr.random) 
        #     itr = itr.next

        # return hmap[head]


        ## O(1) solution works with atleast 1 node
        if head == None:
            return None

        itr = head
        while itr:
            itr.next = Node(itr.val, itr.next)
            itr = itr.next.next

        itr = head
        while itr:
            itr.next.random = itr.random.next if itr.random else None ## IMP to check. Because if original node points to None then there is no copy node of it
            itr = itr.next.next

        itr = head
        new_head = head.next ## IMP 2nd list would be broken. So store it

        while itr:
            nxt = itr.next
            itr.next = itr.next.next
            nxt.next = nxt.next.next if nxt.next else None ## IMP to check
            itr = itr.next

        return new_head