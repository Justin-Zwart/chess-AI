from minmax import minmax
import chess


board = chess.Board()

# game loop
while True:
    board.push(minmax(4, True, board, -100000, 100000))
    board.push(input())
