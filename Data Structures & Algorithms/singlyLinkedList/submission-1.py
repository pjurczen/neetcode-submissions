class Node:
    def __init__(self, val: int, next: Node | None = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        i: int = 0
        while cur != None and i < index:
            cur = cur.next
            i += 1
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        self.head = Node(val=val, next=self.head)
        if self.tail is None:
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        tail = self.tail
        new = Node(val=val)
        if tail:
            tail.next = new
        else:
            self.head = new
        self.tail = new

    def remove(self, index: int) -> bool:
        prev, cur = None, self.head
        i: int = 0
        while cur != None and i < index:
            prev = cur
            cur = cur.next
            i += 1
        if cur is None:
            return False
        if prev != None:
            prev.next = cur.next
        if cur == self.head:
            self.head = cur.next
        if cur == self.tail:
            self.tail = prev
        return True

    def getValues(self) -> List[int]:
        cur = self.head
        result = []
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        return result
