class Node:
    def __init__(self, key = None, val = None, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, key, val):
        if len(self.map) == self.cap:
            self.remove(self.map[self.head.next.key])
        node = Node(key=key, val=val,prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.map[key] = node
    
    def remove(self, node):
        node = self.map[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.map[node.key]


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node.key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        self.insert(key,value)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)