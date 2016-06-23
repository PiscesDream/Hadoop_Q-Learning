from games import PickNumber, PickNumberWithRange, TicTacToe
from common import Game
from players import RandomPlayer, QPlayer
import cPickle

if __name__ == '__main__':
#   game = Game('Pick Number', PickNumberWithRange(50))
    game = Game('Tic-Tac-Toe', TicTacToe()) 
    qp1 = QPlayer('Robot', './qvalues/tictactoe.qvalues', epsilon=0.5)  
    rp1 = RandomPlayer('Alice')
    rp2 = RandomPlayer('Bob')

    FILE_COUNT = 20
    REC_PER_FILE = 1000

    for i in range(FILE_COUNT):
        with open('input/data.{}.dat'.format(i), 'w') as f:
            for j in range(REC_PER_FILE):
                print 'simulating game {} ...\r'.format(j),
                res = game.play([rp1, rp2])[(i+2)%2]
                f.write('0\t0\t0\n')
                for move in res:
                    f.write('{}\t{}\t{}\n'.format(move[1], move[0], move[2]))
                    # status, action, value

