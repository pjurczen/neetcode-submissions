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
        self.head, self.tail = QueueNode(-1, -1), QueueNode(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.queue = {}

    def get(self, key: int) -> int:
        #print('- - -')
        #print(f'get(key={key})')
        #print(f'Before: {self._getCacheOrder()}')
        if key in self.queue:
            node: QueueNode = self.queue[key]
            self._remove(node)
            #print(f'During: {self._getCacheOrder()}')
            self._insert(node)
            #print(f'After: {self._getCacheOrder()}')
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #print('- - -')
        #print(f'put(key={key}, val={value})')
        #print(f'Before: {self._getCacheOrder()}')
        if key in self.queue:
            self._remove(self.queue[key])
        new_node = QueueNode(key=key, val=value)
        self._insert(new_node)
        if len(self.queue) > self.capacity:
            lru = self.head.next
            self._remove(lru)
        #print(f'After: {self._getCacheOrder()}')

    def _insert(self, node: QueueNode) -> None:
        next, prev = self.tail, self.tail.prev
        next.prev = prev.next = node
        node.next = next
        node.prev = prev
        self.queue[node.key] = node

    def _remove(self, node: QueueNode) -> None:
        next, prev = node.next, node.prev
        next.prev, prev.next = prev, next
        del self.queue[node.key]

    def _getCacheOrder(self) -> list[tuple[int, int, int, int]]:
        result = []
        cur = self.head
        while cur:
            result.append((cur.key, cur.val, cur.next.val if cur.next else None, cur.prev.val if cur.prev else None))
            cur = cur.next
        return result



