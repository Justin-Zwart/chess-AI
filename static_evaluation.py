def static_evaluation(board_fen):
    evaluation = 0

    for i in range(len(board)):
        # white pieces 
        if board_fen[i] == 'Q':
            evaluation += 9
        if board_fen[i] == 'R':
            evaluation += 5
        if board_fen[i] == 'N':
            evaluation += 3
        if board_fen[i] == 'B':
            evaluation += 3
        if board_fen[i] == 'P':
            evaluation += 1

        # black pieces
        if board_fen[i] == 'q':
            evaluation -= 9
        if board_fen[i] == 'r':
            evaluation -= 5
        if board_fen[i] == 'n':
            evaluation -= 3
        if board_fen[i] == 'b':
            evaluation -= 3
        if board_fen[i] == 'p':
            evaluation -= 1


    return evaluation

