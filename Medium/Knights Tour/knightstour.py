class Board:
    dx = (-2, -2, -1, -1, 1, 1, 2, 2)
    dy = (1, -1, 2, -2, 2, -2, 1, -1)

    def __init__(self):
        self.board = []
        self.visited = []
        while True:
            try:
                x, y = input("Enter your board dimensions: ").split()
                self.rows = int(y)
                self.cols = int(x)
                if self.rows > 0 and self.cols > 0:
                    break
                print("Invalid dimensions!")
            except ValueError:
                print("Invalid dimensions!")
        self.square_length = len(str(self.rows * self.cols))
        one_square = "_" * self.square_length
        for _ in range(self.rows):
            self.board.append([one_square for _ in range(self.cols)])
            self.visited.append([False for _ in range(self.cols)])
        self.row_just = len(str(self.rows))
        self.knight_row = -1
        self.knight_col = -1

    def print_board(self):
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

    def set_knight(self):
        while True:
            try:
                x, y = input("Enter the knight's starting position: ").split()
                x = int(x)
                y = int(y)
                if 1 <= x <= self.cols and 1 <= y <= self.rows:
                    square = ((self.square_length - 1) * " ") + "X"
                    self.knight_row = self.rows - y
                    self.knight_col = x - 1
                    self.board[self.knight_row][self.knight_col] = square
                    self.visited[self.knight_row][self.knight_col] = True
                    break
                print("Invalid position!")
            except ValueError:
                print("Invalid position!")

    def mark_knight_moves(self):
        for i in range(8):
            new_knight_x = self.knight_row + Board.dx[i]
            new_knight_y = self.knight_col + Board.dy[i]
            if 0 <= new_knight_x < self.rows and 0 <= new_knight_y < self.cols:
                count = self.count_moves(new_knight_x, new_knight_y)
                square = ((self.square_length - 1) * " ") + str(count)
                self.board[new_knight_x][new_knight_y] = square

    def count_moves(self, row, col):
        count = 0
        for i in range(8):
            new_knight_x = row + Board.dx[i]
            new_knight_y = col + Board.dy[i]
            if 0 <= new_knight_x < self.rows and 0 <= new_knight_y < self.cols:
                count += not self.visited[new_knight_x][new_knight_y]
        return count


def main():
    board = Board()
    board.set_knight()
    board.mark_knight_moves()
    print("\nHere are the possible moves:")
    board.print_board()


if __name__ == "__main__":
    main()
