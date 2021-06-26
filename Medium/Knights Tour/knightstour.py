class Board:
    def __init__(self):
        self.board = []
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
        self.row_just = len(str(self.rows))

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
                    self.board[self.rows - y][x - 1] = square
                    break
                print("Invalid position!")
            except ValueError:
                print("Invalid position!")


def main():
    board = Board()
    board.set_knight()
    board.print_board()


if __name__ == "__main__":
    main()
