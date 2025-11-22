from typing import List
import queue

class M695:
    def maxAreaOfIslandBFS(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        q = queue.Queue()
        max_area = 0
        for i in range(m):
            for j in range(n):
                current_area = 0
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    q.put((i, j))
                    current_area += 1
                    while q.qsize() > 0:
                        x, y = q.get()
                        left = y - 1
                        right = y + 1
                        up = x - 1
                        down = x + 1
                        if left >= 0 and grid[x][left] == 1 and (x, left) not in visited:
                            visited.add((x, left))
                            q.put((x, left))
                            current_area += 1 
                        if right < n and grid[x][right] == 1 and (x, right) not in visited:
                            visited.add((x, right))
                            q.put((x, right))
                            current_area += 1
                        if up >= 0 and grid[up][y] == 1 and (up, y) not in visited:
                            visited.add((up, y))
                            q.put((up, y))
                            current_area += 1
                        if down < m and grid[down][y] == 1 and (down, y) not in visited:
                            visited.add((down, y))
                            q.put((down, y))
                            current_area += 1
                    if current_area > max_area:
                        max_area = current_area
        return max_area
    
    def dfs(self, i: int, j: int) -> int:
        m = len(self.grid)
        n = len(self.grid[0])
        if i >= 0 and i < m and j >=0 and j < n and self.grid[i][j] == 1 and (i, j) not in self.visited:
            self.visited.add((i, j))
            up = j -1
            down = j + 1
            right = i -1
            left = i + 1
            return 1 + self.dfs(i, up) + self.dfs(i, down) + self.dfs(left, j) + self.dfs(right, j)
        else:
            return 0


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        m = len(grid)
        n = len(grid[0])
        self.visited = set()

        max_area = 0
        for i in range(m):
            for j in range(n):
                current_area = 0
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    current_area = self.dfs(i, j)
                    if current_area > max_area:
                        max_area = current_area

        return max_area