class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.lastIdx = -1


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        newIdx = self.lastIdx + 1
        if self.getCapacity() <= newIdx:
            self.resize()
        self.arr[self.lastIdx + 1] = n
        self.lastIdx = newIdx


    def popback(self) -> int:
        item = self.arr[self.lastIdx]
        self.lastIdx -= 1
        return item
 

    def resize(self) -> None:
        curLen = len(self.arr)
        for _ in range(curLen):
            self.arr.append(None)


    def getSize(self) -> int:
        return self.lastIdx + 1
        
    
    def getCapacity(self) -> int:
        return len(self.arr)
