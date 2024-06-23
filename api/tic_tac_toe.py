# api/tic_tac_toe.py

import os

class TicTacToe:

    def __init__(self):
        self.board = [' '] * 10

    def clearoutput(self):
        os.system('cls' if os.name == 'nt' else "clear")

    def display_board(self):
        self.clearoutput()
        return f"""
           |     |  
        {self.board[1]}  |  {self.board[2]}  | {self.board[3]}
        ___|_____|___ 
           |     |  
        {self.board[4]}  |  {self.board[5]}  | {self.board[6]}
        ___|_____|___
           |     |  
        {self.board[7]}  |  {self.board[8]}  | {self.board[9]}
           |     |  
        """

    def player_input(self):
        marker = ''
        while marker.lower() != 'x' and marker.lower() != 'o':
            marker = input('Please enter O or X: ')

        if marker.lower() == 'x':
            return 'X', 'O'
        else:
            return 'O', 'X'

    def win_check(self, board, mark):
        return ((board[1] == mark and board[2] == mark and board[3] == mark) or
                (board[4] == mark and board[5] == mark and board[6] == mark) or
                (board[7] == mark and board[8] == mark and board[9] == mark) or
                (board[1] == mark and board[4] == mark and board[7] == mark) or
                (board[2] == mark and board[5] == mark and board[8] == mark) or
                (board[3] == mark and board[6] == mark and board[9] == mark) or
                (board[1] == mark and board[5] == mark and board[9] == mark) or
                (board[3] == mark and board[5] == mark and board[7] == mark))

    def space_checker(self, board, position):
        return board[position] == ' '

    def marker_placer(self, board, position, mark):
        board[position] = mark

    def player_choice(self, board):
        while True:
            try:
                position = int(input('Place your marker, enter 1-9: '))
                if position in range(1, 10) and self.space_checker(board, position):
                    return position
                else:
                    print('Invalid input or position already taken. Please enter a valid position (1-9).')
            except ValueError:
                print("Invalid input. Please enter a number (1-9).")

    def replay(self):
        play = input('Do you want to play again? Press "y" for Yes: ')
        return play.lower() == 'y'

def handler(request):
    tictoe = TicTacToe()
    while True:
        board = [' '] * 10
        player1, player2 = tictoe.player_input()
        turn = 'player1'

        while True:
            if turn == 'player1':
                tictoe.display_board()
                position = tictoe.player_choice(board)
                tictoe.marker_placer(board, position, player1)
                if tictoe.win_check(board, player1):
                    tictoe.display_board()
                    print("Player 1 has won!")
                    break
                elif ' ' not in board[1:]:
                    tictoe.display_board()
                    print('Match Tied')
                    break
                else:
                    turn = 'player2'
            else:
                tictoe.display_board()
                position = tictoe.player_choice(board)
                tictoe.marker_placer(board, position, player2)
                if tictoe.win_check(board, player2):
                    tictoe.display_board()
                    print("Player 2 has won!")
                    break
                elif ' ' not in board[1:]:
                    tictoe.display_board()
                    print('Match Tied')
                    break
                else:
                    turn = 'player1'
        if not tictoe.replay():
            break

    return {
        'statusCode': 200,
        'body': 'Game Over'
    }
