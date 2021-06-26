def get_coordinates():
    """Get the knight's starting position from the user"""
    while True:
        try:
            x, y = input("Enter the knight's starting position: ").split()
            x = int(x)
            y = int(y)
            if 1 <= x <= 8 and 1 <= y <= 8:
                return 8 - y, x - 1
        except ValueError:
            print("Invalid dimensions!")
        else:
            print("Invalid dimensions!")


def print_board(board):
    print(" -------------------")
    print("8|", *board[0], "|")
    print("7|", *board[1], "|")
    print("6|", *board[2], "|")
    print("5|", *board[3], "|")
    print("4|", *board[4], "|")
    print("3|", *board[5], "|")
    print("2|", *board[6], "|")
    print("1|", *board[7], "|")
    print(" -------------------")
    print("   1 2 3 4 5 6 7 8")


def main():
    board = []
    for _ in range(8):
        board.append(list("________"))
    x, y = get_coordinates()
    board[x][y] = "X"
    print_board(board)


if __name__ == "__main__":
    main()
