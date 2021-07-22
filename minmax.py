from static_evaluation import static_evaluation
import chess


# check if end of game has been achieved
def outcome_achieved(board):
    if board.can_claim_fifty_moves():
        print("oiasdfasdf")
        return True
    if board.is_stalemate():
        print("low elo noobscrub can't checkmate with queen and king")
        return True
    if board.is_insufficient_material():
        print("sadge")
        return True
    if board.is_checkmate():
        print('gggggg')
        return True
    
    return False


# recursively check for best moves
def minmax(depth, max_to_play, board, alpha, beta):
    if depth == 0 or outcome_achieved(board):
        print("still this issue")
        return static_evaluation(board)

    print(12341234123412344)
    if max_to_play:
        print("maxplayin")
        max_eval = -100000
        for i in board.legal_moves:
            max_eval = max(max_eval, minmax(depth - 1, False, board.push(i), alpha, beta)[0])
            alpha = max(alpha, max_eval)
            if alpha >= beta:
                break

        return [max_eval, i]

    else:
        min_eval = 100000
        print("min")
        for i in board.legal_moves:
            min_eval = min(min_eval, minmax(depth - 1, True, board.push(i), alpha, beta)[0])
            beta = min(beta, min_eval)
            if alpha >= beta:
                break
    
        return [min_eval, i]

