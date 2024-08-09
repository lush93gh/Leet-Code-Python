from typing import List

class HeapSort():

    def left(self, i: int) -> int:
        return i << 1
    
    def right(self, i: int) -> int:
        return (i << 1) + 1
    
    def exchange(self, A: List[int], i: int, j: int):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp
    
    def maxHeapify(self, A: List[int], i: int):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l <= self.heapSize and A[l] > A[i]:
            largest = l
        if r <= self.heapSize and A[r] > A[largest]:
            largest = r

        if largest != i:
            self.exchange(A, i, largest)
            self.maxHeapify(A, largest)

    def buildMaxHeap(self, A: List[int], n: int):
        self.heapSize = n
        for i in range(n >> 1, 0, -1):
            self.maxHeapify(A, i)

    def heapSort(self, A: List[int], n: int):
        self.buildMaxHeap(A, n)
        for i in range(n, 1, -1):
            self.exchange(A, i, 1)
            self.heapSize -= 1
            self.maxHeapify(A, 1)

    def sort(self, A: List[int]) -> List[int]:
        A.insert(0, 0)
        self.heapSort(A, len(A) - 1)
        return A[1:]
