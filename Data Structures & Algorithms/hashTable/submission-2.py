class Pair:

    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value

class HashTable:

    _DELETED = "__DELETED__"
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = []
        for _ in range(capacity):
            self.map.append(None)

    def insert(self, key: int, value: int) -> None:
        idx: int = self._findIdx(key)
        if idx != -1:
            self.map[idx].value = value
        else:
            idx = self.hash(key) % self.capacity
            while self.map[idx] is not None:
                idx += 1
                idx = idx % self.capacity
            self.size += 1
            self.map[idx] = Pair(key=key, value=value)
            if self.size / self.capacity >= 0.5:
                self.resize()
    
    def _findIdx(self, key: int) -> int:
        idx: int = self.hash(key) % self.capacity
        while self.map[idx] is not None:
            slot = self.map[idx]
            if slot != self._DELETED and slot.key == key:
                return idx
            else:
                idx += 1
                idx = idx % self.capacity
        return -1

    def get(self, key: int) -> int:
        idx: int = self._findIdx(key)
        return self.map[idx].value if idx != -1 else -1
                
    def hash(self, key: int) -> int:
        return key # identity function for integer

    def remove(self, key: int) -> bool:
        idx: int = self._findIdx(key)
        if idx == -1:
            return False
        self.map[idx] = self._DELETED
        self.size -= 1
        return True

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_map = []
        self.capacity *= 2
        for _ in range(self.capacity):
            new_map.append(None)
        
        self.size = 0
        tmp = self.map
        self.map = new_map
        for oldEntry in tmp:
            if oldEntry is not None and oldEntry != self._DELETED:
                self.insert(oldEntry.key, oldEntry.value)


