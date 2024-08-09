from typing import List

class M79:
    def exist(self, board: List[List[str]], word: str) -> bool:
        first = word[0]
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == first:
                    queue = []
                    visited = set()
                    queue.append(board[i][j])
                    # AI Labs Coding