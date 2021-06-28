def get_ints(prompt, error, x_min=-float("inf"), x_max=float("inf"),
             y_min=-float("inf"), y_max=float("inf")):
    while True:
        try:
            x, y = [int(num) for num in input(prompt).split()]
            if x_min <= x <= x_max and y_min <= y <= y_max:
                return x, y
            print(error)
        except ValueError:
            print(error)


class Board:
    dx = (-2, -2, -1, -1, 1, 1, 2, 2)
    dy = (1, -1, 2, -2, 2, -2, 1, -1)

    def __init__(self, rows, cols):
        self.board = []
        self.visited = []
        self.rows, self.cols = rows, cols
        self.square_length = len(str(self.rows * self.cols))
        one_square = "_" * self.square_length
        for _ in range(self.rows):
            self.board.append([one_square for _ in range(self.cols)])
            self.visited.append([False for _ in range(self.cols)])
        self.row_just = len(str(self.rows))
        self.knight_row = -1
        self.knight_col = -1
        self.knight_moves = ()

    def print_board(self):
        self.mark_knight_moves()
        top_len = self.cols * (self.square_length + 1) + 3
        print(" " * self.row_just + "-" * top_len)
        for i in range(self.rows):
            line_start = str(self.rows - i).rjust(self.row_just) + "|"
            print(line_start, *self.board[i], "|")
        print(" " * self.row_just + "-" * top_len)
        print(" " * (self.row_just + 2), end="")
        for num in range(1, self.cols + 1):
            num_str = str(num).rjust(self.square_length)
            print(num_str + " ", end="")
        print()

    def set_knight(self, x, y):
        self.knight_row, self.knight_col = self.convert_coordinates(x, y)
        self.visited[self.knight_row][self.knight_col] = True
        self.knight_moves = self.get_moves(self.knight_row, self.knight_col)

    def mark_knight_moves(self):
        square_prefix = (self.square_length - 1) * " "
        for x, row in enumerate(self.board):
            for y, square in enumerate(row):
                if x == self.knight_row and y == self.knight_col:
                    self.board[x][y] = square_prefix + "X"
                elif self.visited[x][y]:
                    self.board[x][y] = square_prefix + "*"
                elif (x, y) in self.knight_moves:
                    count = len(self.get_moves(x, y))
                    self.board[x][y] = square_prefix + str(count)
                else:
                    self.board[x][y] = self.square_length * "_"

    def move_knight(self, row, col):
        row, col = self.convert_coordinates(row, col)
        if (row, col) in self.knight_moves:
            self.visited[row][col] = True
            self.knight_row = row
            self.knight_col = col
            self.knight_moves = self.get_moves(row, col)
            return True
        return False

    def get_moves(self, row, col):
        moves = []
        for i in range(8):
            x = row + Board.dx[i]
            y = col + Board.dy[i]
            if 0 <= x < self.rows and 0 <= y < self.cols:
                if not self.visited[x][y]:
                    moves.append((x, y))
        return tuple(moves)

    def count_visited(self):
        count = 0
        for row in self.visited:
            for is_visited in row:
                count += is_visited
        return count

    def convert_coordinates(self, row, col):
        return self.rows - col, row - 1


def main():
    cols, rows = get_ints("Enter your board dimensions: ",
                          "Invalid dimensions", x_min=1, y_min=1)
    board = Board(rows, cols)
    x, y = get_ints("Enter the knight's starting position: ",
                    "Invalid position!", 1, board.cols, 1, board.rows)
    board.set_knight(x, y)
    board.print_board()

    while board.knight_moves != ():
        print()
        x, y = get_ints("Enter your next move: ", "Invalid move!",
                        1, board.cols, 1, board.rows)
        while not board.move_knight(x, y):
            x, y = get_ints("Invalid Move! Enter your next move: ",
                            "Invalid Move! Enter your next move: ",
                            1, board.cols, 1, board.rows)
        board.print_board()
    num_visited = board.count_visited()
    if num_visited < board.rows * board.cols:
        print("\nNo move possible moves!")
        print(f"Your knight visited {num_visited} squares!")
    else:
        print("\nWhat a great tour! Congratulations!")


if __name__ == "__main__":
    main()
