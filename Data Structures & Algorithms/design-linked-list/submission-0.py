class ListNode:

    def __init__(self, val: int, next: "ListNode" | None = None, prev: "ListNode" | None = None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return f"Val: {self.val}, Next: {self.next.val if self.next else None}, Prev: {self.prev.val if self.prev else None}"

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
        

    def get(self, index: int) -> int:
        node = self.head
        for _ in range(1, index + 1):
            if not node:
                return -1
            node = node.next
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return None
        elif index == self.len:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            #print("addAtIndex")
            #self._print()
            node = self.head
            for _ in range(1, index + 1):
                node = node.next
            new_node = ListNode(val=val, next=node, prev=node.prev)
            node.prev.next = new_node
            node.prev = new_node
            #self._print()
            self.len += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < self.len:
            if index == 0:
                self.head = self.head.next
            elif index == self.len - 1:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                #print("deleteAtIndex")
                #self._print()
                node = self.head
                for _ in range(1, index + 1):
                    node = node.next
                #print(f"Found: {node}")
                node.prev.next = node.next
                node.next.prev = node.prev
                #self._print()
            self.len -= 1
        
    def _print(self):
        print("Start")
        head = self.head
        while head:
            print(head)
            head = head.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)