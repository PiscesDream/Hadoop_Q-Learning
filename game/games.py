'''
    To define a game, we only have to define GameState 
'''

from common import GameState
from copy import deepcopy
import random

class PickNumber(GameState):
    '''
        Pick number from 0~N-1,
            who pick secret number wins.
    '''
    def __init__(self, N):
        self.N = N

    def init(self, players):
        self.checked = [None] * self.N 
        self.valid = set(range(self.N))
        self.secret = random.randint(0, self.self.N-1)
        self.players = players

    def validMoves(self):
        return self.valid

    def update(self, player, move):
        # check validity
        assert move in self.valid
        self.checked[move] = self.players.index(player)
        self.valid.discard(move)

    def score(self, player):
        if self.checked[self.secret] == self.players.index(player):
            return +100.0 
        else:
            return 0.0

    def output(self):
        print self.checked, ':', self.secret

    def isEnd(self):
        return self.secret not in self.valid

    def serialize(self, player):
        # from player's perspecitve, his/she is always 0
        player_index = self.players.index(player)

        def reindex(index):
            if index == None:
                return None
            elif index == player_index:
                return 0
            elif index < player_index:
                return index+1
            elif index > player_index:
                return index
        def index2str(index):
            if isinstance(index, int):
                return str(index)
            else:
                return '^'
        return ''.join(map(index2str, map(reindex, self.checked)))

class PickNumberWithRange(GameState):
    '''
        Pick number from 0~N-1,
            who pick secret number wins.
    '''
    def __init__(self, N):
        self.N = N

    def init(self, players):
        self.left = 0
        self.right = self.N-1
        self.checked = [None] * self.N 
        self.secret = random.randint(0, self.N-1)
        self.players = players

    def validMoves(self):
        return range(self.left, self.right+1)

    def update(self, player, move):
        # check validity
        assert move in self.validMoves()
        self.checked[move] = self.players.index(player)
        if move > self.secret:
            self.right = move-1
        elif move < self.secret:
            self.left = move+1
        else:
            self.right = self.left = self.secret

    def score(self, player):
        if self.checked[self.secret] == self.players.index(player):
            return +100.0 
        else:
            return 0.0

    def output(self):
        print '{}~{} : {}'.format(self.left, self.right, self.secret)

    def isEnd(self):
        return self.checked[self.secret] != None

    def serialize(self, player):
        # from player's perspecitve, his/she is always 0
        player_index = self.players.index(player)

        def reindex(index):
            if index == None:
                return None
            elif index == player_index:
                return 0
            elif index < player_index:
                return index+1
            elif index > player_index:
                return index
        def index2str(index):
            if isinstance(index, int):
                return str(index)
            else:
                return '^'
        return ''.join(map(index2str, map(reindex, self.checked)))

       



class TicTacToe(GameState):
    '''
        Classic TicTacToe
    '''
    def __init__(self):
        pass

    def init(self, players):
        self.players = players
        self.board = [None]*9 
        self.valid = set(range(9))

    def validMoves(self):
        return self.valid
            

    def update(self, player, move):
        # check validity
        assert move in self.validMoves()
        self.board[move] = self.players.index(player)
        self.valid.discard(move)

    def score(self, player):
        player_index = self.players.index(player)
        if self.board[0] == self.board[1] == self.board[2] == player_index or \
           self.board[3] == self.board[4] == self.board[5] == player_index or \
           self.board[6] == self.board[7] == self.board[8] == player_index or \
           self.board[0] == self.board[3] == self.board[6] == player_index or \
           self.board[1] == self.board[4] == self.board[7] == player_index or \
           self.board[2] == self.board[5] == self.board[8] == player_index or \
           self.board[0] == self.board[4] == self.board[8] == player_index or \
           self.board[2] == self.board[4] == self.board[6] == player_index:
            return +100.0
        else:
            return 0.0

    def output(self):
        print '==='
        print self.board[0:3]
        print self.board[3:6]
        print self.board[6:9]
        print '==='

    def isEnd(self):
        return any([self.score(player) for player in self.players]) or len(self.validMoves())==0

    def serialize(self, player):
        # from player's perspecitve, his/she is always 0
        player_index = self.players.index(player)

        def reindex(index):
            if index == None:
                return None
            elif index == player_index:
                return 0
            elif index < player_index:
                return index+1
            elif index > player_index:
                return index
        def index2str(index):
            if isinstance(index, int):
                return str(index)
            else:
                return '^'
        return ''.join(map(index2str, map(reindex, self.board)))
        

