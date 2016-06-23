from common import Player
import math
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


class QPlayer(Player):
    '''
        QPlayer makes decision on Qvalues table
    '''
    def __init__(self, name, qvfile, epsilon=0.0):
        super(QPlayer, self).__init__(name)
        self.epsilon = epsilon

        self.Qvalue = {}
        with open(qvfile, 'r') as f:
            for line in f:
                state, action, qvalue = line.strip().split()
                self.Qvalue[(state, action)] = float(qvalue)

    def prepare(self):
        pass

    def play(self, state):
        # check from table
        actions = list(state.validMoves())
        qvalues = [self.Qvalue.get((str(state.serialize(self)), str(action)), 0.0) for action in actions]
        if random.random() < self.epsilon:
            # soft-max normalize
            qvalues = map(lambda x: math.exp(x), qvalues)
            qvalues = map(lambda x: x / sum(qvalues), qvalues)
            # random
            r = random.random()
            acc = 0.0
            for action, probability in zip(actions, qvalues):
                acc += probability
                if acc > r: return action
        else:
            return actions[qvalues.index(max(qvalues))]

    def __repr__(self):
        return '<QPlayer: {}>'.format(self.name)


