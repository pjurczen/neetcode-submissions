from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.heap) == 1:
            self.heap.append(val)
            return val
        if len(self.heap) < self.k + 1:
            # no k elements in heap yet
            # add, reconcile structure and ordering be percolating up
            self.heap.append(val)
            i: int = len(self.heap) - 1
            while i > 1 and self.heap[i] < self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
                i = i // 2
            # and return the root
        elif val > self.heap[1]:
            # k elements already in heap
            # check if new element is larger than root (min value)
            # if its smaller, nothing to do -> return root
            # if its greater, add new element to the heap by replacing the root with it
            self.heap[1] = val
            i: int = 1
            while i < len(self.heap):
                if (
                        2 * i + 1 < len(self.heap)
                        and self.heap[2 * i + 1] < self.heap[i]
                        and self.heap[2 * i + 1] < self.heap[2 * i]
                ):
                    # right child exists
                    # and it is smaller than the parent
                    # and right child is smaller than left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif 2 * i < len(self.heap) and self.heap[2 * i] < self.heap[i]:
                    # left child exists
                    # and it is smaller than the parent
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    # parent is already smaller than its both children
                    break
            # and then percolating the root down to reconcile the ordering
            # and return the root
        return self.heap[1]
