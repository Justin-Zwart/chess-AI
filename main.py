
from minmax import minmax
import chess


board = chess.Board()
for i in board.legal_moves:
    print(i) 
