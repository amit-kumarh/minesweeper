import copy

class Board:
    def __init__(self, num, val = ' '):
        self.board = [[copy.deepcopy(val) for j in range(num)] for i in range(num)]

    def drawBoard(self):
        print('--------'*len(self.board))
        for row in self.board:
            print('|\t' * (len(row)+1))
            for tile in row:
                print(f'|   {tile}   ', end='')
            print('|')
            print('|\t' * (len(row)+1))
            print('--------'*len(self.board))