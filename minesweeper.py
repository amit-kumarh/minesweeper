from board import Board
from tile import Tile, Bomb
import random

class MineSweeper(Board):
    def __init__(self, numBombs, dimensions):
        super().__init__(dimensions, Tile(' ', False))
        self._generateBombs(numBombs)
        self._generateNumbers()

    def _generateBombs(self, numBombs):
        for i in range(numBombs):
            bomb_set = False
            while not bomb_set:
                x = random.randint(0, len(self.board)-1)
                y = random.randint(0, len(self.board)-1)
                if type(self.board[y][x]) != Bomb:
                    self.board[y][x] = Bomb()
                bomb_set = True

    def _generateNumbers(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if type(self.board[i][j]) != Bomb:
                    count = 0
                    if i > 0 and type(self.board[i-1][j]) == Bomb:
                        count += 1
                    if i < len(self.board)-1 and type(self.board[i+1][j]) == Bomb :
                        count += 1
                    if j > 0 and type(self.board[i][j-1]) == Bomb:
                        count += 1
                    if j < len(self.board[i])-1 and type(self.board[i][j+1]) == Bomb:
                        count += 1
                    if i < len(self.board)-1 and j < len(self.board[i])-1 and type(self.board[i+1][j+1]) == Bomb:
                        count += 1
                    if i > 0 and j > 0 and type(self.board[i-1][j-1]) == Bomb:
                        count += 1
                    if i > 0 and j < len(self.board[i])-1 and type(self.board[i-1][j+1]) == Bomb:
                        count += 1
                    if i < len(self.board)-1 and j > 0 and type(self.board[i+1][j-1]) == Bomb:
                        count += 1
                    self.board[i][j].setValue(str(count))

    def flip(self, i, j):
        self.board[i][j].flip()
    
    def flag(self, i, j):
        self.board[i][j].flag()

    def checkWin(self):
        for row in self.board:
            for cell in row:
                if type(cell) == Tile and cell.visible == False:
                    return False
        return True
    
    def checkLoss(self, i, j):
        if type(self.board[int(i)][int(j)]) == Bomb:
            return True
        else:
            return False
        










                

