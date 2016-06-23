from games import PickNumber, PickNumberWithRange, TicTacToe
from common import Game
from players import RandomPlayer, HumanPlayer, QPlayer

if __name__ == '__main__':
#   game = Game('Pick Number', PickNumber(50))
#   game = Game('Pick Number', PickNumberWithRange(50))
    game = Game('Tic-Tac-Toe', TicTacToe()) 

    # random vs random
    rp1 = RandomPlayer('Alice')
    rp2 = RandomPlayer('Bob')
    res = game.play([rp1, rp2], verbose=1)
    print res

    # human vs random
#   hp1 = HumanPlayer('Me')
#   res = game.play([hp1, rp1])
#   print res


    # qlearning 
    qp1 = QPlayer('Robot', './qvalues/tictactoe.qvalues', epsilon=0.3)
    qp2 = QPlayer('Robot', './qvalues/tictactoe.qvalues', epsilon=0.3)
    
    win = tie = loss = 0
    for i in xrange(1000):
        # second move
        res = game.play([qp1, qp2], shuffle=False)

        # first move 
#       res = game.play([qp1, rp1], shuffle=False)

        if len(res[1]) == 0 or res[0][-1][-1] == 100:
            win += 1
        elif len(res[0]) == 0 or res[0][-1][-1] == 0:
            loss += 1
        else:
            tie += 1
        print 'win = {}, tie = {}, loss = {}'.format(win, tie, loss)

        
