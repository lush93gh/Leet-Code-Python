from typing import List
import queue


class M200:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [['0' for _ in range(n)] for _ in range(m)]
        q = queue.Queue()
        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == '0':
                    visited[i][j] = '1'
                    q.put((i, j))
                    island_count += 1
                    while not q.empty():
                        land = q.get()
                        x, y = land
                        up = x - 1
                        if up >= 0 and grid[up][y] == '1' and visited[up][y] == '0':
                            visited[up][y] = '1'
                            q.put((up, y))
                        down = x + 1
                        if (
                            down < m
                            and grid[down][y] == '1'
                            and visited[down][y] == '0'
                        ):
                            visited[down][y] = "1"
                            q.put((down, y))
                        left = y - 1
                        if (
                            left >= 0
                            and grid[x][left] == '1'
                            and visited[x][left] == '0'
                        ):
                            visited[x][left] = '1'
                            q.put((x, left))
                        right = y + 1
                        if (
                            right < n
                            and grid[x][right] == '1'
                            and visited[x][right] == '0'
                        ):
                            visited[x][right] = '1'
                            q.put((x, right))

        return island_count
    
a = M200()
print(
    a.numIslands(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
) # 1
print(
    a.numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
) # 3
