from common import Player
import random

class RandomPlayer(Player):
    '''
        A random player
    '''
    def prepare(self):
        pass

    def play(self, state):
        return random.choice(list(state.validMoves()))

    def __repr__(self):
        return '<RandomPlayer: {}>'.format(self.name)



class HumanPlayer(Player):
    '''
        A random player
    '''
    def prepare(self):
        pass

    def play(self, state):
        validMoves = list(state.validMoves())
        res = raw_input('Pick one move from {}: '.format(dict(zip(range(len(validMoves)), validMoves))))
        res = int(res)
        assert 0 <= res < len(validMoves)
        res = validMoves[res]
        return res 

    def __repr__(self):
        return '<HumanPlayer: {}>'.format(self.name)



