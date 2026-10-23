class CalendarNode:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.left = None
        self.right = None
    
    def book(self, start: int, end: int) -> bool:
        if start < self.end and self.start < end:
            return False
        if end <= self.start:
            if self.left is None:
                self.left = CalendarNode(start, end)
                return True
            else:
                return self.left.book(start, end)
        else:
            if self.right is None:
                self.right = CalendarNode(start, end)
                return True
            else:
                return self.right.book(start, end)

class MyCalendar:
    
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if self.root is None:
            self.root = CalendarNode(startTime, endTime)
            return True
        return self.root.book(startTime, endTime)

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)