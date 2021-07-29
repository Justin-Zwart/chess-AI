from static_evaluation import static_evaluation
from board_update import board_update
import chess


# check if end of game has been achieved
def outcome_achieved(board):
    if board.can_claim_fifty_moves():
        return True
    if board.is_stalemate():
        return True
    if board.is_insufficient_material():
        return True
    if board.is_checkmate():
        return True
    
    return False


# recursively check for best moves
def minmax(depth, max_to_play, board_san, board_fen, alpha, beta):
    if depth == 0 or outcome_achieved(board_san):
        return static_evaluation(board_fen)

    if max_to_play:
        max_eval = -100000
        for i in board_san.legal_moves:
            max_eval = max(max_eval, minmax(depth - 1, False, board_san.push(i), board_update(board_san, board_fen, i), alpha, beta)[0])
            alpha = max(alpha, max_eval)
            if alpha >= beta:
                break

        return [max_eval, i]

    else:
        min_eval = 100000
        for i in board_san.legal_moves:
            min_eval = min(min_eval, minmax(depth - 1, True, board_san.push(i), board_update(board_san, board_fen, i), alpha, beta)[0])
            beta = min(beta, min_eval)
            if alpha >= beta:
                break
    
        return [min_eval, i]

