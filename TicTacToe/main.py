from tictactoe import TicTacToe

if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
    while True:
        print('\n Would you like to play again?')
        print(f'1. Yes, please!')
        print(f'2. No, thank you!')
        choice = input('> ')

        if choice not in ['1', '2']:
            print('Option not available.')
        elif int(choice) == 1:
            tic_tac_toe.start()
        else:
            print("GAME OVER!")
            break

