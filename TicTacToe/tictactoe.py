from players import Player
from hello_function import greeting_the_player


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_players_name(self):
        player_1 = Player()
        greeting_the_player(player_1)

        player_2 = Player()
        greeting_the_player(player_2)

        while True:
            print('Who will start first?')
            print(f'1. {player_1.name}')
            print(f'2. {player_2.name}')
            choice = input('> ')

            if choice not in ['1', '2']:
                print('Option not available.')
            else:
                break

        if choice == '1':
            print(f'{player_1} will start the game!')

            return True
        else:
            print(f'{player_2} will start the game!')
            return False

    def fill_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_winning(self, player):
        win = None

        n = len(self.board)

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def change_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def clear_board(self):
        self.board = []

    def start(self):
        self.create_board()

        player = 'X' if self.get_players_name() == bool(1) else 'O'
        while True:
            print(f" Is player {player} turn")
            self.show_board()
            row, col = list(
                map(int, input("Enter 'row-column' numbers to fix the spot: ").split("-")))
            print()
            self.fill_spot(row - 1, col - 1, player)
            if self.is_player_winning(player):
                print(f"Player {player} wins the game!")
                break
            if self.is_board_filled():
                print("Match ended with a draw!")
                break
            player = self.change_player_turn(player)

        print()
        self.show_board()
        self.clear_board()
