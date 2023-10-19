from board import Board
import time


board = Board(10, 10)
board.place_cell(5, 2)
board.place_cell(5, 3)
board.place_cell(5, 4)

while True:
    time.sleep(1)
    print(board)
    board.next()
