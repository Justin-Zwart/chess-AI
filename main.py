from minmax import minmax
import chess

white = True
board = chess.Board()

# game loop
if white:
    while True:
        move = minmax(4, True, board, -100000, 100000)
        board.push(move)
        print(move)
        board.push(input())
else:
    while True:
        board.push(input())
        move = minmax(4, True, board, -100000, 100000)
        board.push(move)
        print(move)
