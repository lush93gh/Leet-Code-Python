from typing import List
import queue

class M79:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                cursor = 0
                if board[i][j] == word[cursor]:
                    if self.dfs(i, j , board, word, 0):
                        return True
        return False


    def dfs(self, i: int, j :int, board: List[List[str]], word: str, cursor: int):   
        m = len(board)
        n = len(board[0])

        if i< 0 or i >=m or j < 0 or j >= n or cursor >= len(word) or word[cursor] != board[i][j]:
            return False     
        elif word[cursor] == board[i][j]: 
            board[i][j] = ord(board[i][j]) ^ 256

            if cursor == len(word) - 1:
                return True
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                if x >= 0 and x <m and y >=0 and y <n:
                    if self.dfs(x, y, board, word, cursor + 1):
                        return True 
                    
            board[i][j] = chr(board[i][j] ^ 256)

        return False
     
    def existBFS(self, board: List[List[str]], word: str) -> bool:
        """Have bugs"""
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                visited = set()
                q = queue.Queue()
                cursor = 0
                if board[i][j] == word[cursor] and (i, j) not in visited:
                    # print('outter', i, j , board[i][j])
                    visited.add((i, j))
                    q.put((i, j, cursor, visited))
                    while not q.empty():
                        for _ in range(q.qsize()):
                            coord = q.get()
                            x, y, current_cursor, current_visited = coord
                            current_cursor = len(current_visited) 
                            if len(current_visited) == len(word):
                                return True
                            # print(x, y, board[x][y], current_cursor, current_visited)
                            up = x - 1
                            if (
                                up >= 0
                                and board[up][y] == word[current_cursor]
                                and (up, y) not in current_visited
                            ):
                                cv = current_visited.copy()
                                cv.add((up, y))
                                q.put((up, y, current_cursor, cv))
                            down = x + 1
                            if (
                                down < m
                                and board[down][y] == word[current_cursor]
                                and (down, y) not in current_visited
                            ):
                                cv = current_visited.copy()
                                cv.add((down, y))
                                q.put((down, y, current_cursor, cv))
                            left = y - 1
                            if (
                                left >= 0
                                and board[x][left] == word[current_cursor]
                                and (x, left) not in current_visited
                            ):
                                cv = current_visited.copy()
                                cv.add((x, left))
                                q.put((x, left, current_cursor, cv))
                            right = y + 1
                            if (
                                right < n
                                and board[x][right] == word[current_cursor]
                                and (x, right) not in visited
                            ):
                                cv = current_visited.copy()
                                cv.add((x, right))
                                q.put((x, right, current_cursor, cv))
                    
        return False
    
a = M79()
# a = 'A'
# print(chr(ord(a) ^ 256 ^ 256))
print(
    a.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
) # True
print(
    a.exist(
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
        word = "SEE"
    )
) # True
print(
    a.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
) # False
print(
    a.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
        word="ABCESEEEFS",
    )
) # True
print(
    a.exist(
        board=[["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]],
        word="aaaaaaaaaaaaa",
    )
) # False
print(
    a.exist(
        board=[
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
        ],
        word="AAAAAAAAAAAAAAB",
    )
) # False
