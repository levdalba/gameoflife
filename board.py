class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[False] * width for i in range(height)]

    def __str__(self):
        rv = ""
        for row in self.board:
            rv += "".join(".0"[int(C)] for C in row) + "\n"
        return rv

    def place_cell(self, row, col):
        self.board[row][col] = True

    def next(self):
        self.new_board = [[False] * self.width for i in range(self.height)]
        for row_num in range(self.width):
            for col_num in range(self.height):
                n = self.get_num_neighbor(row_num, col_num)
                if not self.board[row_num][col_num]:
                    if n == 3:
                        self.new_board[row_num][col_num] = True
                else:
                    if n == 2 or n == 3:
                        self.new_board[row_num][col_num] = True
        tmp = self.board
        self.board = self.new_board
        self.new_board = tmp

    def get_num_neighbor(self, row, col):
        counter = 0
        for r in (-1, 0, 1):
            for c in (-1, 0, 1):
                if not (r == 0 and c == 0):
                    if 0 <= row + r < self.height and 0 <= col + c < self.width:
                        if self.board[row + r][col + c]:
                            counter += 1

        return counter
