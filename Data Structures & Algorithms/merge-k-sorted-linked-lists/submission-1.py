# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        min_heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        dummy = ListNode()
        copy = dummy

        while min_heap:
            val, idx, node = min_heap[0]
            heapq.heappop(min_heap)

            dummy.next = node
            dummy = dummy.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        return copy.next
        
