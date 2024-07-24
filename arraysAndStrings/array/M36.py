from typing import List

class M36:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            checksum_row = 0
            checksum_col = 0
            checksum_box = 0
            for j in range(9):
                e = row[j]
                if e == ".":
                    continue
                elif checksum_row | (1 << (int(e) - 1)) == checksum_row:
                    return False
                else:
                    checksum_row = checksum_row | (1 << (int(e) - 1))
            for j in range(9):
                e = board[j][i]
                if e == ".":
                    continue
                elif checksum_col | (1 << (int(e) - 1)) == checksum_col:
                    return False
                else:
                    checksum_col = checksum_col | (1 << (int(e) - 1))
            
            for j in range(9):
                e = board[i%3*3 + j//3][j%3 + i//3*3]
                if e == ".":
                    continue
                elif checksum_box | (1 << (int(e) - 1)) == checksum_box:
                    return False
                else:
                    checksum_box = checksum_box | (1 << (int(e) - 1))
        return True

a = M36()
print(a.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(a.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))