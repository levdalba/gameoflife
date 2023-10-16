class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[False] * width for i in range(height)]

    def as_str(self):
        rv = ""
        for row in self.board:
            rv += "".join(".0"[C] for C in row) + "\n"

            rv += "\n"
        return rv


board = Board(3, 3)
print(board.as_str())
