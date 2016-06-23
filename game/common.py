import random
from copy import deepcopy

class GameState(object):
    '''
        Abstract class for state of a specific game
    '''

    def __init__(self):
        raise NotImplemented

    def init(self, players):
        '''
            Initialize state
        '''
        raise NotImplemented

    def validMoves(self):
        '''
            return list of valid moves given current state 
        '''
        raise NotImplemented

    def update(self, player, move):
        '''
            Update state with move executed by player
        '''
        assert move in self.validMoves

        raise NotImplemented

    def score(self, player):
        '''
            Calculate current score of a player given current state
            Generally, a higher score is better
        '''
        raise NotImplemented

    def output(self):
        '''
            To print a specific state, like (in tic-tac-toe):
                #####
                #.o.#
                #xx.#
                #.ox#
                #####
        '''
        raise NotImplemented 

    def isEnd(self):
        '''
            Return (a boolean) whether the game is over.
        '''
        raise NotImplemented

    def serialize(self, player):
        '''
            From the point of view of a player,
            use a number/list/dictionary/string to represent current state
                so that we can record it in serial.
        '''
        raise NotImplemented


class Game(object):
    '''
        Host a game with given type of GameState
    '''
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def play(self, players, shuffle=True, verbose=0):
        '''
            Start and record a game.
        '''

        # prepare players 
        for player in players: player.prepare()
        NOF = len(players) # number of players

        # shuffle the order of players
        if shuffle:
            random.shuffle(players)

        # initailze the game state
        state = deepcopy(self.state)
        state.init(players)

        history = [[] for player in players]
        iteration = 0
        while not state.isEnd():
            old_state = state.serialize(player)

            # output current game
            if verbose > 0:
                state.output()

            # make a move 
            player = players[iteration % NOF]
            move = player.play(state)

            # update game state
            state.update(player, move)

            # record
            history[iteration % NOF].\
                append( (move, old_state, state.score(player)) ) 
            
            iteration += 1


        if verbose > 0:
            # output last state
            state.output()

            # output result
            for player in players:
                print '{} score: {}\n'.format(player, state.score(player))
        return history
        
    def __repr__(self):
        return '<Game: {}>'.format(self.name)


class Player(object):
    '''
        Abstract class for a player
    '''
    def __init__(self, name):
        self.name = name

    def prepare(self):
        '''
            Prepare before a game
        '''
        raise NotImplemented 

    def play(self, state):
        '''
            Given a specific game state,
                a player should make their move.
        '''
        raise NotImplemented

    def __repr__(self):
        return '<Player: {}>'.format(self.name)
