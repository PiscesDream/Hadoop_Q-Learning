from games import TicTacToe
from common import Game
from players import RandomPlayer
import cPickle

if __name__ == '__main__':
    game = Game('Tic-Tac-Toe', TicTacToe()) 
    rp1 = RandomPlayer('Alice')
    rp2 = RandomPlayer('Bob')

    FILE_COUNT = 10
    REC_PER_FILE = 100

    for i in range(FILE_COUNT):
        data = []
        for j in range(REC_PER_FILE):
            print 'simulating game {} ...'.format(j)
            res = game.play([rp1, rp2])
            if res[0][-1][-1] == 100.0:
                data.append(res[0])
            elif res[1][-1][-1] == 100.0:
                data.append(res[1])

        cPickle.dump(data, open('input/data.{}.dat'.format(i), 'wb'), True)
