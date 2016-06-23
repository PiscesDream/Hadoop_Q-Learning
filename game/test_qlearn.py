from games import TicTacToe
from common import Game
from players import RandomPlayer, QPlayer
import sys

def test(players):
    win = tie = loss = 0
    for i in xrange(1000):
        res = game.play(players, shuffle=False)
        if len(res[1]) == 0 or res[0][-1][-1] == 100:
            win += 1
        elif len(res[0]) == 0 or res[0][-1][-1] == 0:
            loss += 1
        else:
            tie += 1
        print 'win = {}, tie = {}, loss = {}\r'.format(win, tie, loss),
    return (win, tie, loss)

if __name__ == '__main__':
    game = Game('Tic-Tac-Toe', TicTacToe()) 

    rp1 = RandomPlayer('Alice')
    qp1 = QPlayer('Robot', sys.argv[1], epsilon=0.3)

    first_move = test([qp1, rp1])
    print '==============As first move====================='
    print 'win = {}, tie = {}, loss = {}'.format(*first_move)

    second_move = test([rp1, qp1])
    print '==============As second move===================='
    print 'win = {}, tie = {}, loss = {}'.format(*second_move)
        
