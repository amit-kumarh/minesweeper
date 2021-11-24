from minesweeper import MineSweeper

def main():
    game = MineSweeper(5, 5)
    while True:
        game.drawBoard()
        if game.checkWin():
            print('Congratulations! You won!')
            break

        print('Please input move (row, column, flag)')
        move = input('>')
        if len(move) == 2:
            game.flip(int(move[0]), int(move[1]))
            if game.checkLoss(move[0], move[1]):
                game.drawBoard()
                print('You Lost')
                break
        elif len(move) == 3 and move[2].lower() == 'f':
            game.flag(int(move[0]), int(move[1]))
        else:
            print("Wrong input - please try again")
            continue



if __name__ == "__main__":
    main()