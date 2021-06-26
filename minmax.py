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


def minmax(depth, max_to_play, board, alpha, beta):
    if depth == 0 or outcome_achieved(board):
        return static_evaluation(board)

    if max_to_play:
        max_eval = -100000
        for i in board.legal_moves:
            max_eval = max(max_eval, minmax(depth - 1, False, board.push(i), alpha, beta))
            alpha = max(alpha, max_eval)
            if alpha >= beta:
                break

        return max_eval

    else:
        min_eval = 100000
        for i in board.legal_moves:
            min_eval = min(min_eval, minmax(depth - 1, True, board.push(i), alpha, beta))
            beta = min(beta, min_eval)
            if alpha >= beta:
                break
    
        return min_eval

