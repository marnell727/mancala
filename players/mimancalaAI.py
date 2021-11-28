from players.MancalaAI import MancalaAI

class MiMancalaAI(MancalaAI):

    def get_move(self, board):
        valid_moves = board.get_valid_moves()
        my_mancala_idx = 0 if self.player_num == 2 else 7
        # opp_mancala_idx = 7 if self.player_num == 2 else 0
        max_score = -1
        max_score_move = -1
        go_again = 1
        for move in valid_moves:
            score = self.get_move_r(move)
            if score > max_score:
                max_score = score
                max_score_move = move
        return max_score_move

    def get_move_r(self, move, board, my_mancala_idx):
        test_board = board.get_test_board(move)
        if test_board.player_num == self.player_num:
            valid_moves = test_board.get_valid_moves()
            for move in valid_moves:
                self.get_move_r(valid_moves, test_board, my_mancala_idx)
        else:
            number_of_stones_in_pit = test_board.board[my_mancala_idx]
            score = number_of_stones_in_pit
            return score