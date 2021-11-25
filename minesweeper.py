from board import Board
from tile import Tile, Bomb
import random

class MineSweeper(Board):
    '''
    Class that represents a Minesweeper board and game. Subclass of Board.

    Attributes
    ----------
    numBombs: int
        Number of bombs to generate in the grid
    
    See parent function for more.

    Methods
    -------
    flip(i, j)
        Reveals the tile located at row i and column j

    flag(i, j)
        Toggles the flag of the tile located at row i and column j

    checkWin() -> bool
        Checks if the game is won (ie. there are no hidden non-mine squares remaining)

    checkLoss(i, j) -> bool
        Checks if the game is lost on a particular move (if the tile at row i and column j is a mine)

    isVisible(i, j) -> bool
        Checks if the tile at row i and column j is visible

    instructions()
        Prints game instructions

    '''
    def __init__(self, numBombs, dimensions):
        '''
        Constructs all necessary attributes and populates board with mines and numbers.

        Parameters
        ----------
        numBombs: int
            Number of bombs to generate in the grid

        dimensions: int
            Length of each size of the game Board
        '''
        super().__init__(dimensions, Tile(' ', False))
        self._generateBombs(numBombs)
        self._generateNumbers()

    def _generateBombs(self, numBombs):
        '''
        Generates and populates game board with mines.
        
        Parameters
        ----------
        numBombs: int
            Number of bombs to generate in the grid

        Returns
        -------
        None
        '''
        for i in range(numBombs):
            bomb_set = False
            while not bomb_set:
                x = random.randint(0, len(self.board)-1)
                y = random.randint(0, len(self.board)-1)
                if type(self.board[y][x]) != Bomb:
                    self.board[y][x] = Bomb()
                bomb_set = True

    def _generateNumbers(self):
        '''
        Populates the game board (with bombs present) with the appropriate numbers.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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
        '''
        Reveals appropriate tiles after the player plays a given move. 
        Operates recursively to automaticlally reveal any tiles surrounding a visible 0.

        Parameters
        ----------
        i: int
            row of move
        
        j: int
            column of move

        Returns
        -------
        None
        '''
        self.board[i][j].flip()
        if self.board[i][j].value == '0':
                 if i > 0 and not self.isVisible(i-1, j):
                    self.flip(i-1, j)
                 if i < len(self.board)-1 and not self.isVisible(i+1, j):
                    self.flip(i+1, j)
                 if j > 0 and not self.isVisible(i, j-1):
                    self.flip(i, j-1)
                 if j < len(self.board)-1 and not self.isVisible(i, j+1):
                    self.flip(i, j+1)
                 if i < len(self.board)-1 and j < len(self.board[i])-1 and not self.isVisible(i+1, j+1):
                    self.flip(i+1, j+1)
                 if i > 0 and j > 0 and not self.isVisible(i-1, j-1):
                    self.flip(i-1, j-1)
                 if i > 0 and j < len(self.board[i])-1 and not self.isVisible(i-1, j+1):
                    self.flip(i-1, j+1)
                 if i < len(self.board)-1 and j > 0 and not self.isVisible(i+1, j-1):
                    self.flip(i+1, j-1)

    def flag(self, i, j):
        '''Toggles the flag state of the tile located at row i and column j'''
        self.board[i][j].flag()

    def checkWin(self):
        '''Checks if the game is won (ie. there are no hidden non-mine squares remaining), returns boolean'''
        for row in self.board:
            for cell in row:
                if type(cell) == Tile and cell.visible == False:
                    return False
        return True
    
    def checkLoss(self, i, j):
        '''Checks if the game is lost on a particular move (if the tile at row i and column j is a mine), returns boolean'''
        if type(self.board[i][j]) == Bomb:
            return True
        else:
            return False

    def isVisible(self, i, j):
        '''Checks if the tile at row i and column j is visible, returns boolean'''
        return self.board[i][j].visible

    def instructions(self):
        '''Prints game instructions'''
        print('''To play, type in the coordinates of the board square you would like to flip as two digits
with no commas or other characters (ex. 11). To flag a square as a mine, simply type an 'f' after 
the square's coordinates (ex. 11f).''')
            
        










                

