class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[False for _ in range(width)] for _ in range(height)]

    def is_alive(self, row, col):
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return False
        return self.cells[row][col]

    def place_cell(self, row, col):
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return
        self.cells[row][col] = True

    def remove_cell(self, row, col):
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return
        self.cells[row][col] = False

    def toggle_cell(self, row, col):
        if self.is_alive(row, col):
            self.remove_cell(row, col)
        else:
            self.place_cell(row, col)

    def count_neighbors(self, row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i == row and j == col:
                    continue
                if self.is_alive(i, j):
                    count += 1
        return count

    def next(self):
        new_cells = [[False for _ in range(self.width)] for _ in range(self.height)]
        for row in range(self.height):
            for col in range(self.width):
                count = self.count_neighbors(row, col)
                if self.is_alive(row, col):
                    if count == 2 or count == 3:
                        new_cells[row][col] = True
                else:
                    if count == 3:
                        new_cells[row][col] = True
        self.cells = new_cells

    def __str__(self):
        return "\n".join(
            "".join(".o"[self.cells[row][col]] for col in range(self.width))
            for row in range(self.height)
        )
