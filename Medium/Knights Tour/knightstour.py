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
        self.knight_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                self.knight_moves.append((i, j))
        self.knight_moves = tuple(self.knight_moves)
        self.moves = []

    def print_board(self, board=None):
        if board is None:
            self.mark_knight_moves()
            board = self.board
        top_len = self.cols * (self.square_length + 1) + 3
        print(" " * self.row_just + "-" * top_len)
        for i in range(self.rows):
            line_start = str(self.rows - i).rjust(self.row_just) + "|"
            print(line_start, *board[i], "|")
        print(" " * self.row_just + "-" * top_len)
        print(" " * (self.row_just + 2), end="")
        for num in range(1, self.cols + 1):
            num_str = str(num).rjust(self.square_length)
            print(num_str + " ", end="")
        print()

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

    def move_knight(self, row, col, convert=True):
        if convert:
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
        return sum([sum([v for v in row]) for row in self.visited])

    def convert_coordinates(self, row, col):
        return self.rows - col, row - 1

    def print_solution(self):
        self.moves = [["0" for _ in range(self.cols)] for _ in range(self.rows)]
        if self.has_solution() and self.solve(1):
            for i, row in enumerate(self.moves):
                for j, move in enumerate(row):
                    prefix = (self.square_length - len(str(move))) * " "
                    self.moves[i][j] = prefix + str(move)
            print("\nHere's the solution!")
            self.print_board(self.moves)
        else:
            print("No solution exists!")

    def has_solution(self):
        x, y = min(self.rows, self.cols), max(self.rows, self.cols)
        return x >= 5 or (x, y) in ((3, 4), (4, 5))

    def solve(self, moves_made):
        self.moves[self.knight_row][self.knight_col] = str(moves_made)
        if moves_made == self.rows * self.cols:
            return True
        current_knight_moves = tuple(self.knight_moves)
        cur_row, cur_col = self.knight_row, self.knight_col
        for move in current_knight_moves:
            self.move_knight(move[0], move[1], False)
            if self.solve(moves_made + 1):
                return True
            self.visited[cur_row][cur_col] = False
            self.visited[move[0]][move[1]] = False
            self.knight_moves = self.get_moves(move[0], move[1])
            self.move_knight(cur_row, cur_col, False)
        return False


def main():
    cols, rows = get_ints("Enter your board dimensions: ",
                          "Invalid dimensions", x_min=1, y_min=1)
    board = Board(rows, cols)
    x, y = get_ints("Enter the knight's starting position: ",
                    "Invalid position!", 1, board.cols, 1, board.rows)
    board.move_knight(x, y)

    try_puzzle = input("Do you want to try the puzzle? (y / n): ")
    while try_puzzle != "y" and try_puzzle != "n":
        print("Invalid option!")
        try_puzzle = input("Do you want to try the puzzle? (y / n): ")

    if not board.has_solution():
        print("No solution exists!")
    elif try_puzzle == "y":
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
    else:
        board.print_solution()


if __name__ == "__main__":
    main()
