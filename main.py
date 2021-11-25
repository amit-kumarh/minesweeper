from minesweeper import MineSweeper
import time

def main():
    #Loop to choose difficulty
    while True:
        difficulty = input('Please select difficulty - (e)asy, (m)edium, or (h)ard\n>')
        if difficulty[0].lower() == 'e':
            game = MineSweeper(5, 5)
            break
        elif difficulty[0].lower() == 'm':
            game = MineSweeper(20,8)
            break
        elif difficulty[0].lower() == 'h':
            game = MineSweeper(35, 10)
            break
        else:
            print('Invalid difficulty - please try again')

    start_time = time.time()    # Starting game timer
    game.instructions()
    while True:
        game.drawBoard()
        if game.checkWin():
            end_time = time.time()
            time_elapsed = round(end_time - start_time, 2)
            print(f'Congratulations! You won in {time_elapsed} seconds!')
            break

        print('Please input move (row, column, flag)')
        move = input('>')
        try:
            row = int(move[0])-1    # Accounting for 0 indexing
            col = int(move[1])-1
        except:
            print('Bad input - please try again')
            continue
        if len(move) == 2  and 0 <= row <= len(game.board)-1 and 0 <= col <= len(game.board)-1: # check for valid move
            game.flip(row, col)
            if game.checkLoss(row, col):
                game.drawBoard()
                print('You Lost')
                break
        elif len(move) == 3 and move[2].lower() == 'f' and 0 <= row <= len(game.board)-1 and 0 <= col <= len(game.board)-1:
            game.flag(row, col)
        else:
            print("Bad input - please try again")
            continue



if __name__ == "__main__":
    main()
