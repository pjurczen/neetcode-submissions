from collections import deque

class MyStack:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
        

    def push(self, x: int) -> None:
        if len(self.stack1) > 0:
            self.stack2.append(x)
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.popleft())
        else:
            self.stack1.append(x)
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.popleft())

    def pop(self) -> int:
        if len(self.stack1) > 0:
            return self.stack1.popleft()
        elif len(self.stack2) > 0:
            return self.stack2.popleft()

    def top(self) -> int:
        if len(self.stack1) > 0:
            return self.stack1[0]
        elif len(self.stack2) > 0:
            return self.stack2[0]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()