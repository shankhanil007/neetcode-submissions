class ListNode:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.order = ListNode(-1, -1, None, None)
        self.hmap = defaultdict()
        self.size = 0
        self.capacity = capacity
        self.tail = self.order
        self.head = self.order
        
    def get(self, key: int) -> int:    
        if key in self.hmap.keys():
            value = self.hmap[key].value
            self.remove(self.hmap[key])
            self.put(key, value)
            return value
        return -1

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt 
        if nxt:                    ## If you are removing the last node then None to prev connection not needed
            nxt.prev = prev
        if self.head == node:      ## IMP
            self.head = nxt
        if self.tail == node:      ## IMP
            self.tail = prev
        self.size -= 1
        self.hmap.pop(node.key)    ## IMP that's why we store both key and value in node
                    
    def put(self, key: int, value: int) -> None:
        if key in self.hmap.keys():   ### IMP scenario
            self.remove(self.hmap[key])  ### IMP scenario. Not just update. Remove and add
            self.put(key, value)

        elif self.size < self.capacity:
            node = ListNode(key, value, self.tail, None)
            self.tail.next = node
            self.hmap[key] = node
            if self.size == 0:   ## IMP
                self.head = node
            self.tail = node
            self.size += 1
            
        else:
            self.remove(self.head)
            self.put(key, value)
            


