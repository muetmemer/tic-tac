import os


class TicTacToe:

    def __init__(self):
        self.board = [' ']*10

    # Clearing the screen
    def clearoutput(self):
        os.system('cls' if os.name == 'nt' else "clear")

    # Displaying the board
    def display_board(self):
        self.clearoutput()
        print("   |     |  ")
        print(self.board[1]+'  |  '+self.board[2]+'  | '+self.board[3])
        print('___|_____|___ ')
        print("   |     |  ")
        print(self.board[4]+'  |  '+self.board[5]+'  | '+self.board[6])
        print('___|_____|___')
        print("   |     |  ")
        print(self.board[7]+'  |  '+self.board[8]+'  | '+self.board[9])
        print("   |     |  ")

    # Function for players to choose X or O
    def player_input(self):
        marker = ''
        while marker.lower() != 'x' and marker.lower() != 'o':
            marker = input('Please enter O or X: ')

        if marker.lower() == 'x':
            return ('X', 'O')
        else:
            return ('O', 'X')

    # Checking if a player has won the game
    def win_check(self, board, mark):
        # Winning combinations on the board
        return ((board[1] == mark and board[2] == mark and board[3] == mark) or
                (board[4] == mark and board[5] == mark and board[6] == mark) or
                (board[7] == mark and board[8] == mark and board[9] == mark) or
                (board[1] == mark and board[4] == mark and board[7] == mark) or
                (board[2] == mark and board[5] == mark and board[8] == mark) or
                (board[3] == mark and board[6] == mark and board[9] == mark) or
                (board[1] == mark and board[5] == mark and board[9] == mark) or
                (board[3] == mark and board[5] == mark and board[7] == mark))

    # Checking if a space on the board is available
    def space_checker(self, board, position):
        # Check if the specified position on the board is empty
        return board[position] == ' '

    # Placing a marker on the board
    def marker_placer(self, board, position, mark):
        # Place the player's marker on the board at the specified position
        board[position] = mark

    # Function for players to choose their move
    def player_choice(self, board):
        while True:
            try:
                position = int(input('Place your marker, enter 1-9: '))
                if position in range(1, 10) and self.space_checker(board, position):
                    return position
                else:
                    print('''Invalid input or position already taken. Please
                          enter a valid position (1-9).''')
            except ValueError:
                print("Invalid input. Please enter a number (1-9).")

    # Asking if players want to play again
    def replay(self):
        play = input('Do you want to play again? Press "y" for Yes: ')
        return play.lower() == 'y'


if __name__ == '__main__':
    print("Welcome to the Tic Tac Toe game!")

    # Initialize TicTacToe object
    tictoe = TicTacToe()

    while True:
        # Initialize the game board
        board = [' '] * 10

        # Players choose their markers (X or O)
        player1, player2 = tictoe.player_input()

        # Start with player 1
        turn = 'player1'

        while True:
            if turn == 'player1':
                # Display the current board
                tictoe.display_board(board)

                # Player 1's turn
                position = tictoe.player_choice(board)
                tictoe.marker_placer(board, position, player1)

                # Check if player 1 has won
                if tictoe.win_check(board, player1):
                    tictoe.display_board(board)
                    print("Player 1 has won!")
                    break
                # Check if the board is full (tie)
                elif ' ' not in board[1:]:
                    tictoe.display_board(board)
                    print('Match Tied')
                    break
                else:
                    # Switch turn to player 2
                    turn = 'player2'
            else:
                # Display the current board
                tictoe.display_board(board)

                # Player 2's turn
                position = tictoe.player_choice(board)
                tictoe.marker_placer(board, position, player2)

                # Check if player 2 has won
                if tictoe.win_check(board, player2):
                    tictoe.display_board(board)
                    print("Player 2 has won!")
                    break
                # Check if the board is full (tie)
                elif ' ' not in board[1:]:
                    tictoe.display_board(board)
                    print('Match Tied')
                    break
                else:
                    # Switch turn back to player 1
                    turn = 'player1'

        # Ask players if they want to play again
        if not tictoe.replay():
            break
