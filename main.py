from board import Board
import time

board = Board(3, 3)
board.place_cell(0, 1)
board.place_cell(1, 1)
board.place_cell(2, 1)


while True:
    time.sleep(1)
    print(board)
    board.next()
