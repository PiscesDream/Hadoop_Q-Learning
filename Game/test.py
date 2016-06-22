from games import PickNumber, PickNumberWithRange, TicTacToe
from common import Game
from players import RandomPlayer, HumanPlayer

if __name__ == '__main__':
#   game = Game('Pick Number', PickNumber(50))
#   game = Game('Pick Number', PickNumberWithRange(50))
    game = Game('Tic-Tac-Toe', TicTacToe()) 

    # random vs random
    rp1 = RandomPlayer('Alice')
    rp2 = RandomPlayer('Bob')
    res = game.play([rp1, rp2])
    print res

    # human vs random
    hp1 = HumanPlayer('Me')
    res = game.play([hp1, rp1])
    print res

