class Node:

    def __init__(self, value: int, next: 'Node | None' = None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f"Node(value={self.value}, next={self.next})"

class Queue:

    def __init__(self, elements: list[int]):
        self.head = None
        self.tail = None
        self.len = 0
        for el in elements:
            self.enqueue(el)
    
    def enqueue(self, element: int) -> None:
        node = Node(value=element)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.len += 1

    def dequeue(self) -> int:
        curr = self.head
        self.head = self.head.next
        self.len -= 1
        return curr.value

    def peek(self) -> int | None:
        return self.head.value if self.head else None

    def __str__(self) -> str:
        elements: int = []
        tmp = self.head
        while tmp:
            elements.append(tmp.value)
            tmp = tmp.next
        return str(elements)

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentsQueue = Queue(students)
        sandwichesQueue = Queue(sandwiches)
        while sandwichesQueue.peek() is not None:
            foundSandwich: bool = False
            for _ in range(studentsQueue.len):
                if studentsQueue.peek() == sandwichesQueue.peek():
                    studentsQueue.dequeue()
                    sandwichesQueue.dequeue()
                    foundSandwich = True
                    break
                else:
                    student = studentsQueue.dequeue()
                    studentsQueue.enqueue(student)
            if not foundSandwich:
                break
            else:
                foundSandwich = False
        return sandwichesQueue.len








