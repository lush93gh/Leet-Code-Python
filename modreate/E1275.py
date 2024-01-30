from typing import List
from array import *

class E1275:
    def tictactoe(self, moves: List[List[int]]) -> str:
        flag  = False
        table = [[0,0,0], [0,0,0], [0,0,0]]
        for move in moves: 
            print(move)
            if flag == True:
                table[move[0]][move[1]] = 1
            else:
                table[move[0]][move[1]] = -1
            
            flag = not flag
        
        mainDiagonalSum = 0
        counterDiagonalSum = 0

        for i in range(len(table)):
            row = table[i]
            if sum(row) == len(table):
                return "B"
            elif sum(row) == -len(table):
                return "A"
            
            colSum = 0
            for j in range(len(table)):
                colSum += table[j][i]
            
            if colSum == len(table):
                print("colSum", colSum)
                return "B"
            elif colSum == -len(table):
                return "A"
            
            mainDiagonalSum += table[i][i]
            counterDiagonalSum += table[i][len(table) - 1 - i]

        if mainDiagonalSum == len(table):
            print("mainDiagonalSum")
            return "B"
        elif mainDiagonalSum == -len(table):
            return "A"
        
        if counterDiagonalSum == len(table):
            print("counterDiagonalSum")
            return "B"
        elif counterDiagonalSum == -len(table):
            return "A"
        
        for row in table:
            if 0 in row:
                return "Pending"
            
        return "Draw"

a = E1275()
print(a.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))