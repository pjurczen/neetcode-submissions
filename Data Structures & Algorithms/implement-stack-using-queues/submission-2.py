from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()
        self.top_cache = None
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.top_cache = x

    def pop(self) -> int:
        for _ in range(len(self.stack) - 2):
            self.stack.append(self.stack.popleft())
        self.top_cache = self.stack[0]
        self.stack.append(self.stack.popleft())
        return self.stack.popleft()

    def top(self) -> int:
        return self.top_cache

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()