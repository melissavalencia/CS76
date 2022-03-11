import random
import chess


class MinimaxAI():
    def __init__(self, depth):
        self.depth = depth
        self.nodes_visited = 0
        # pass

    # decision making function
    def choose_move(self, board):
        all_moves = list(board.legal_moves)
        cost = 0
        random.shuffle(all_moves)
        current_move = all_moves[0]

        for move in all_moves:
            board.push(move)
            copy_cost = self.value(board, self.depth, cost)
            if cost < copy_cost:
                cost = copy_cost
                current_move = move
            board.pop()
        print("minimax")
        print("nodes visited:", self.nodes_visited)
        print("depth:", self.depth)
        print("best_move:", current_move)
        return current_move

        # pass

    # evaluation function
    def utility(self, state):
        # pawns
        white_p = len(state.pieces(chess.PAWN, chess.WHITE))
        black_p = len(state.pieces(chess.PAWN, chess.BLACK))
        total_p = abs(white_p - black_p)

        # rooks
        white_r = len(state.pieces(chess.ROOK, chess.WHITE))
        black_r = len(state.pieces(chess.ROOK, chess.BLACK))
        total_r = abs(white_r - black_r) * 5

        # queens
        white_q = len(state.pieces(chess.QUEEN, chess.WHITE))
        black_q = len(state.pieces(chess.QUEEN, chess.BLACK))
        total_q = abs(white_q - black_q) * 9

        # knights
        white_k = len(state.pieces(chess.KNIGHT, chess.WHITE))
        black_k = len(state.pieces(chess.KNIGHT, chess.BLACK))
        total_k = abs(white_k - black_k) * 3

        # bishops
        white_b = len(state.pieces(chess.BISHOP, chess.WHITE))
        black_b = len(state.pieces(chess.BISHOP, chess.BLACK))
        total_b = abs(white_b - black_b) * 3

        utility = total_p + total_r + total_q + total_k + total_b

        return utility

    # determines who the player is and calls respective min/max func
    def value(self, state, depth, cost):
        player = state.turn
        if state.is_checkmate():
            return 1000000000
        if state.is_stalemate():
            return cost
        if player:
            self.nodes_visited += 1
            return self.max_value(state, depth, cost)
        else:
            self.nodes_visited += 1
            return self.min_value(state, depth, cost)

    def max_value(self, state, depth, cost):
        v = float('-inf')
        all_moves = list(state.legal_moves)

        # check cutoff test
        if self.cutoff_test(state, depth):
            print("minimax")
            print("final nodes visited:", self.nodes_visited)
            print("max depth:", depth)
            return self.utility(state)

        for move in all_moves:
            state.push(move)
            v = max(v, self.value(state, depth-1, cost))
            state.pop()
        return v

    def min_value(self, state, depth, cost):
        v = float('inf')
        all_moves = list(state.legal_moves)

        # check cutoff test
        if self.cutoff_test(state, depth):
            return self.utility(state)

        for move in all_moves:
            state.push(move)
            v = min(v, self.value(state, depth-1, cost))
            state.pop()
        return v

    # check if max depth reached or terminal state
    def cutoff_test(self, board, depth):
        if depth == 0 or board.is_game_over():
            return True


