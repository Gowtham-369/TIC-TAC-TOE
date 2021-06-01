import math
import time
from player import HumanPlayer,RandomComputerPlayer,GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = self.make_board() #our board is single list
        self.current_winner = None #keep track of cur winner
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(0,3)]:
            print('| '+' | '.join(row)+' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 (tells us what number corresponds to which spot)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(0,3)]
        for row in number_board:
            print("| "+" | ".join(row)+" |")

    def make_move(self, square, letter):
        # if valid move, then make the move [assign square to letter]
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # total 3 checks
        # across rows
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]

        if (all(spot == letter for spot in row)):
            return True
        #across coloumns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(0, 3)]
        if (all([spot == letter for spot in column])):
            return True
        #across diagonals
        if (square % 2 == 0):
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def empty_squares(self):
        # return any([spot==' ' for spot in self.board])
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ') # count of spaces

    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == " "]
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     # ['X','O','X'] --> [(0,'X'),(1.'O'),(2,'X')]
        #     if spot == ' ':
        #         moves.append(i)

        # return moves

    

def play(game,x_player,o_player,print_game = True):
    
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate till the board has empty squares

    while game.empty_squares():
        #get move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # lets define a function to make a move:
        if game.make_move(square,letter):
            
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter +' wins!')
                return letter
            # we change turn of player
            # letter = (letter^('O'^'X')) # works for char in c++
            letter = 'O' if letter == 'X' else 'X'

        if print_game:
            time.sleep(0.8)

    if print_game:
        print('It\'s a tie!!')


if __name__ == '__main__':

    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
    """
    # check for our correctness,AI never loses
    x_wins,o_wins,ties = 0,0,0
    for _ in range(100):
        t = TicTacToe()
        result = play(t,x_player,o_player,print_game = False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

    print('x_wins are {} , o_wins are {} and ties are {}'.format(x_wins,o_wins,ties))
    """
