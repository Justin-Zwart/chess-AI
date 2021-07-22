def static_evaluation(board):
    board = board.fen()
    evaluation = 0

    for i in range(len(board)):
        # white pieces 
        if board[i] == 'Q':
            evaluation += 9
        if board[i] == 'R':
            evaluation += 5
        if board[i] == 'N':
            evaluation += 3
        if board[i] == 'B':
            evaluation += 3
        if board[i] == 'P':
            evaluation += 1

        # black pieces
        if board[i] == 'q':
            evaluation -= 9
        if board[i] == 'r':
            evaluation -= 5
        if board[i] == 'n':
            evaluation -= 3
        if board[i] == 'b':
            evaluation -= 3
        if board[i] == 'p':
            evaluation -= 1


    return evaluation

