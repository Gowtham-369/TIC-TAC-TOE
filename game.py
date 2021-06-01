import math
import random

class Player():
    def __init__(self,letter):
        # letter is X or O
        self.letter = letter
    
    def get_move(self,game):
        pass




class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter+' \' s turn. Input move [0-8] : ')
            # we will try to typecast into int, if not valid string,gives valueError
            # if not valid in available moves, raise same valueerror
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Not a valid cell.Try again.")
        
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # get sqaure cleverly
            square = self.minimax(game,self.letter)['position']

        return square
    #always use correct keys while using dictinaries,as they won't raise errors
    def minimax(self,state,player):
        max_player = self.letter #yourself!!
        other_player = 'O' if player == 'X' else 'X' #the other player

        #base case
        # we stop if there is a winner in previous state
        if state.current_winner == other_player:
            # we should return position and score, we maximize/minimize score accordingly
            return {'position':None,'score': 1*(state.num_empty_squares()+1) if other_player == max_player else -1*(state.num_empty_squares()+1)}
        
        elif not state.empty_squares():
            #no empty() sqaures
            #winner not decided yet
            # tie
            return {'position' : None,'score': 0}

        if player == max_player:
            best = {'position':None,'score':-math.inf} # each score should maximize 
        else:
            best = {'position':None,'score': math.inf} # we need to minimise at each step

        for possible_move in state.available_moves():
            #step 1: make_move ,try that spot
            state.make_move(possible_move,player)
            #step 2: recursively use minimax to simualte gaem after making that move
            sim_score = self.minimax(state,other_player) #now,we alter player
            #step 3: undo that move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move #messed up if not updated
            #step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score


        return best
