# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from MoveOrderingAlphaBetaAI import MoveOrderingAlphaBetaAI
from IterativeMinimaxAI import IterativeMinimaxAI
from ChessGame import ChessGame


import sys


# player1 = HumanPlayer()
# player2 = RandomAI()
#
# game = ChessGame(player1, player2)
#
# while not game.is_game_over():
#     print(game)
#     game.make_move()

# minimax testing
# player1 = MinimaxAI(1)
# player2 = RandomAI()
# player1 = MinimaxAI(2)
# player2 = RandomAI()
# player1 = MinimaxAI(2)
# player2 = AlphaBetaAI(2)
#
# game = ChessGame(player1, player2)
#
# while not game.is_game_over():
#     print(game)
#     game.make_move()

# alpha beta testing
# player1 = AlphaBetaAI(1)
# player2 = MinimaxAI(1)
# player1 = MinimaxAI(2)
# player2 = AlphaBetaAI(2)

# game = ChessGame(player1, player2)
#
# while not game.is_game_over():
#     print(game)
#     game.make_move()

# move ordering alpha beta testing
# player1 = AlphaBetaAI(1)
# player2 = MoveOrderingAlphaBetaAI(1)
player1 = MoveOrderingAlphaBetaAI(2)
player2 = AlphaBetaAI(2)
# player1 = MinimaxAI(2)
# player2 = MoveOrderingAlphaBetaAI(2)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()


# iterative deepening testing
# player1 = IterativeMinimaxAI(2)
# player2 = AlphaBetaAI(2)
# player1 = AlphaBetaAI(3)
# player2 = IterativeMinimaxAI(3)
# player1 = MoveOrderingAlphaBetaAI(3)
# player2 = IterativeMinimaxAI(3)

# game = ChessGame(player1, player2)
#
# while not game.is_game_over():
#     print(game)
#     game.make_move()


#print(hash(str(game.board)))
