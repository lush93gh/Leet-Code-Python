from typing import List
import heapq


class E2373:
    def __init__(self):
        self.removed_handle = {}

    def heap_remove(self, value):
        count = self.removed_handle.get(value, 0) + 1
        self.removed_handle[value] = count

    def heap_get(self, q) -> int:
        while self.removed_handle.get(q[0], 0) > 0:
            value = heapq.heappop(q)
            count = self.removed_handle.get(value, 0) - 1 
            self.removed_handle[value] = count 
        return q[0] if len(q) > 0 else 0

    def calculate_intersect(self, a, b, x, y):
        if a in range(x, y):
            return range(a, min(b, y))
        elif x in range(a, b):
            return range(x, min(b, y))
        else:
            return range(0)

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        kernel_size = 3
        dimension = len(grid) - kernel_size + 1
        max_pooling = [[0 for _ in range(dimension)] for _ in range(dimension)]
        window = [
            -1 * grid[i][j] for i in range(kernel_size) for j in range(kernel_size)
        ]
        heapq.heapify(window)

        for i in range(dimension):
            for j in range(dimension):
                max_pooling[i][j] = -1 * self.heap_get(window)
                if j < dimension - 1:
                    for k in range(i, i + kernel_size):
                        self.heap_remove(-1 * grid[k][j])
                        heapq.heappush(window, -1 * grid[k][j + kernel_size])
                elif i < dimension - 1:
                    for x in range(i, i + kernel_size):
                        for y in range(j, j + kernel_size):
                            if x in self.calculate_intersect(
                                i, i + kernel_size, i + 1, i + 1 + kernel_size
                            ) and y in self.calculate_intersect(
                                j, j + kernel_size, 0, kernel_size
                            ):
                                continue
                            else:
                                self.heap_remove(-1 * grid[x][y])
                    
                    for x in range(i + 1, i + 1 + kernel_size):
                        for y in range(kernel_size):
                            if x in self.calculate_intersect(
                                i, i + kernel_size, i + 1, i + 1 + kernel_size
                            ) and y in self.calculate_intersect(
                                j, j + kernel_size, 0, kernel_size
                            ):
                                continue
                            else:
                                heapq.heappush(window, -1 * grid[x][y])

        return max_pooling


a = E2373()
# print(a.calculate_intersect(0, 3, 1, 5))
print(a.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
# # [[9,9],[8,6]]
print(
    a.largestLocal(
        grid=[
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
    )
)
# [[2,2,2],[2,2,2],[2,2,2]]
print(
    a.largestLocal(
        [
            [20, 8, 20, 6, 16, 16, 7, 16, 8, 10],
            [12, 15, 13, 10, 20, 9, 6, 18, 17, 6],
            [12, 4, 10, 13, 20, 11, 15, 5, 17, 1],
            [7, 10, 14, 14, 16, 5, 1, 7, 3, 11],
            [16, 2, 9, 15, 9, 8, 6, 1, 7, 15],
            [18, 15, 18, 8, 12, 17, 19, 7, 7, 8],
            [19, 11, 15, 16, 1, 3, 7, 4, 7, 11],
            [11, 6, 5, 14, 12, 18, 3, 20, 14, 6],
            [4, 4, 19, 6, 17, 12, 8, 8, 18, 8],
            [19, 15, 14, 11, 11, 13, 12, 6, 16, 19],
        ]
    )
)
# [
# [20,20,20,20,20,18,18,18],
# [15,15,20,20,20,18,18,18],
# [16,15,20,20,20,15,17,17],
# [18,18,18,17,19,19,19,15],
# [19,18,18,17,19,19,19,15],
# [19,18,18,18,19,20,20,20],
# [19,19,19,18,18,20,20,20],
# [19,19,19,18,18,20,20,20]
#]