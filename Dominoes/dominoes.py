import random

DOMINOES = [[6, 6], [6, 5], [6, 4], [6, 3], [6, 2], [6, 1], [6, 0],
            [5, 5], [5, 4], [5, 3], [5, 2], [5, 1], [5, 0], [4, 4],
            [4, 3], [4, 2], [4, 1], [4, 0], [3, 3], [3, 2], [3, 1],
            [3, 0], [2, 2], [2, 1], [2, 0], [1, 1], [1, 0], [0, 0]]

player = []
computer = []
stock = []
snake = []
player_to_move = "neither"


def deal_dominoes():
    global player, computer, stock
    stock = DOMINOES[:]
    random.shuffle(stock)
    player = stock[0:7]
    computer = stock[7:14]
    stock = stock[14:]


def find_max_double(dominoes):
    max_double = -1
    for domino in dominoes:
        if domino[0] == domino[1] and domino[0] > max_double:
            max_double = domino[0]
    return [max_double, max_double] if max_double >= 0 else []


def find_starting_player():
    global player, computer, snake, player_to_move
    player_double = find_max_double(player)
    computer_double = find_max_double(computer)
    if not player_double and not computer_double:
        return "neither"
    if player_double > computer_double:
        snake.append(player_double)
        player.remove(player_double)
        return False
    snake.append(computer_double)
    computer.remove(computer_double)
    return True


def print_snake():
    global snake
    print()
    if len(snake) > 6:
        print(f"{snake[0]}{snake[1]}{snake[2]}...", end="")
        print(f"{snake[-3]}{snake[-2]}{snake[-1]}")
    else:
        for domino in snake:
            print(domino, end="")
        print()


def print_player_dominoes():
    global player
    print("\nYour pieces:")
    for i, domino in enumerate(player):
        print(f"{i + 1}:{domino}")


def make_move(game_move, hand):
    global stock, snake, player_to_move
    if game_move == 0:
        if len(stock) > 0:
            hand.append(stock.pop())
        player_to_move = not player_to_move
        return True
    domino = hand.pop(abs(game_move) - 1)
    if game_move > 0:
        if snake[-1][-1] not in domino:
            hand.insert(abs(game_move) - 1, domino)
            return False
        else:
            if domino[0] != snake[-1][-1]:
                domino.reverse()
    else:
        if snake[0][0] not in domino:
            hand.insert(abs(game_move) - 1, domino)
            return False
        else:
            if domino[-1] != snake[0][0]:
                domino.reverse()
    snake.insert(0 if game_move < 0 else len(snake), domino)
    player_to_move = not player_to_move
    return True


def end_game():
    global player, computer, snake
    if len(player) == 0:
        print("Status: The game is over. You won!")
        return True
    if len(computer) == 0:
        print("Status: The game is over. The computer won!")
        return True
    count = 0
    if snake[0][0] == snake[-1][-1]:
        num = snake[0][0]
        for domino in snake:
            count += (domino[0] == num) + (domino[1] == num)
    if count == 8:
        print("Status: The game is over. It's a draw!")
        return True
    return False


def is_number(string):
    if string.isdecimal():
        return True
    return string[1:].isdecimal() and string[0] == '-'


def get_move():
    move_string = input()
    while not is_number(move_string) or abs(int(move_string)) > len(player):
        print("Invalid input. Please try again.")
        move_string = input()
    return int(move_string)


while player_to_move == "neither":
    deal_dominoes()
    player_to_move = find_starting_player()

while True:
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    print_snake()
    print_player_dominoes()
    print()
    if end_game():
        break
    if player_to_move:
        print("Status: It's your turn to make a move. Enter your command.")
        move = get_move()
        while not make_move(move, player):
            print("Illegal move. Please try again.")
            move = get_move()
    else:
        print("Status: Computer is about to make a move. "
              "Press Enter to continue...")
        input()
        computer_move = random.randint(-len(computer), len(computer))
        while not make_move(computer_move, computer):
            computer_move = random.randint(-len(computer), len(computer))
