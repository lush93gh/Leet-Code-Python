from typing import List
import random

class QuickSort:
    def exchange(self, A: List[int], i: int, j: int):
        t = A[i]
        A[i] = A[j]
        A[j] = t
    
    def partition(self, A: List[int], p: int, r: int) -> tuple[int, int]:
        x = A[p]
        q = p
        t = p
        for j in range(p + 1, r + 1):
            if A[j] == x:
                t += 1
                self.exchange(A, t, j)
            if A[j] < x:
                self.exchange(A, q, j)
                q += 1
                t += 1
                self.exchange(A, t, j)

        return q, t

    def randomizedPartition(self, A: List[int], p: int, r: int) -> tuple[int, int]:
        i = random.randint(p, r)
        self.exchange(A, i, p)
        return self.partition(A, p, r)
    
    def randomizedQuickSort(self, A: List[int], p: int, r: int):
        if p < r:
            q, t = self.partition(A, p, r)
            self.randomizedQuickSort(A, p, q -1)
            self.randomizedQuickSort(A, t + 1, r)

    def sort(self, A: List[int]) -> List[int]:
        self.randomizedQuickSort(A, 0, len(A) - 1)
        return A