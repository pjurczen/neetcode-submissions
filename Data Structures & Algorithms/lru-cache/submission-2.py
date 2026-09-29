class QueueNode:

    def __init__(self, key: int, val: int, next: 'QueueNode | None' = None, prev: 'QueueNode | None' = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"QueueNode(key={self.key}, val={self.val}, next={self.next.val if self.next else None}, prev={self.prev.val if self.prev else None})"

class LRUCache:

    head: QueueNode | None
    tail: QueueNode | None
    queue: dict[int, QueueNode] # by key

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.queue = {}

    def get(self, key: int) -> int:
        #print('- - -')
        #print(f'get(key={key})')
        #print(f'Before: {self._getCacheOrder()}')
        if key in self.queue:
            node: QueueNode = self.queue[key]
            self._removeFromQueue(node)
            #print(f'During: {self._getCacheOrder()}')
            self._addAtQueueTail(node)
            #print(f'After: {self._getCacheOrder()}')
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #print('- - -')
        #print(f'put(key={key}, val={value})')
        #print(f'Before: {self._getCacheOrder()}')
        if key not in self.queue:
            new_node = QueueNode(key=key, val=value)
            if len(self.queue) == self.capacity:
                self._removeFromQueue(self.head)
            self._addAtQueueTail(new_node)
        else:
            node: QueueNode = self.queue[key]
            node.val = value
            self._removeFromQueue(node)
            self._addAtQueueTail(node)
        #print(f'After: {self._getCacheOrder()}')

    def _addAtQueueTail(self, node: QueueNode) -> None:
        self.queue[node.key] = node
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node
        # empty queue
        if not self.head:
            self.head = node
        # queue too large
        elif len(self.queue) > self.capacity:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        
    def _removeFromQueue(self, node: QueueNode | None) -> None:
        if not node:
            return
        del self.queue[node.key]
        if self.head is node:
            self.head = node.next
        if self.tail is node:
            self.tail = node.prev
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node.next = None
        node.prev = None
        
    def _getCacheOrder(self) -> list[tuple[int, int]]:
        result = []
        cur = self.head
        while cur:
            result.append((cur.key, cur.val, cur.next.val if cur.next else None, cur.prev.val if cur.prev else None))
            cur = cur.next
        return result



