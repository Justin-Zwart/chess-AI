from static_evaluation import static_evaluation
import chess


def outcome_achieved(board):
    if board.can_claim_draw():
        return True
    if board.is_stalemate():
        return True
    if board.is_insufficient_material():
        return True
    if board.is_checkmate():
        return True
    
    return False


def minmax(depth, max_to_play, board):
    if depth == 0 or outcome_achieved(board):
        return static_evaluation(board)

    if max_to_play:
        pass
    else:
        pass
    return 