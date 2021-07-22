from minmax import minmax
from board_update import board_update
import chess

white = True
board_san = chess.Board()
board_fen = chess.Board.fen()

# game loop
if white:
    while True:
        move = minmax(2, False, board_san, board_fen, -100000, 100000)
        board_san, board_fen = board_update(board_san, board_fen, move)
        board_san, board_fen = board_update(board_san, board_fen, input())
else:
    while True:
        board_san, board_fen = board_update(board_san, board_fen, input())
        move = minmax(2, True, board_san, board_fen, -100000, 100000)
        board_san, board_fen = board_update(board_san, board_fen, move)
