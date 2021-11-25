import copy

class Board:
    '''
    Class to represent a square grid-based game board

    Attributes
    ----------

    num: int
        the length of each side of the board

    board: list
        the board object itself

    Methods
    -------

    drawBoard()
        Prints the board onto the console
    '''    
    def __init__(self, num, val = ' '):
        '''
        Constructs the necessary parameters and generates the board object

        Parameters
        ----------
        num: int
            the length of each side of the board

        val: any
            what to fill each grid spot with
        '''
        self.num = num
        self.board = [[copy.deepcopy(val) for j in range(num)] for i in range(num)]

    def drawBoard(self):
        '''Prints board onto the console with labeled row/columns'''
        for i in range(self.num):
            print(f'    {str(i+1)}   ', end='')
        print()
        print('--------'*len(self.board))
        for row in self.board:
            print('|\t' * (len(row)+1))
            for tile in row:
                print(f'|   {tile}   ', end='')
            print(f'|{str(self.board.index(row)+1)}')
            print('|\t' * (len(row)+1))
            print('--------'*len(self.board))