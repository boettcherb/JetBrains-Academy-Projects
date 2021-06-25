class Board:
    def __init__(self, cells):
        self.count_x = cells.count("X")
        self.count_o = cells.count("O")
        self.board = list(cells)

    def __str__(self):
        r1 = " ".join(self.board[0:3])
        r2 = " ".join(self.board[3:6])
        r3 = " ".join(self.board[6:9])
        end = "-" * 9
        return end + "\n| " + r1 + " |\n| " + r2 + " |\n| " + r3 + " |\n" + end

    def valid_board(self):
        """Return False if the current game state is not possible"""
        if abs(self.count_x - self.count_o) > 1:
            return False
        return not self.is_winner("X") or not self.is_winner("O")

    def is_winner(self, player):
        """Return true if player (either "X" or "O") has 3 in a row"""
        for i in range(3):
            if self.board[i:i + 3].count(player) == 3:
                return True
        for i in range(3):
            if self.board[i::3].count(player) == 3:
                return True
        if self.board[::4].count(player) == 3:
            return True
        return self.board[2::2].count(player) == 3

    def evaluate_position(self):
        """Print a message describing the current state of the board"""
        if not self.valid_board():
            print("Impossible")
        elif self.is_winner("X"):
            print("X wins")
        elif self.is_winner("O"):
            print("O wins")
        elif self.count_o + self.count_x == 9:
            print("Draw")
        else:
            print("Game not finished")


def main():
    board = Board(input("Enter cells: "))
    print(board)
    board.evaluate_position()


if __name__ == "__main__":
    main()
