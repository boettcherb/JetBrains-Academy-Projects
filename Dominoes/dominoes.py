import random

DOMINOES = [[6, 6], [6, 5], [6, 4], [6, 3], [6, 2], [6, 1], [6, 0],
            [5, 5], [5, 4], [5, 3], [5, 2], [5, 1], [5, 0], [4, 4],
            [4, 3], [4, 2], [4, 1], [4, 0], [3, 3], [3, 2], [3, 1],
            [3, 0], [2, 2], [2, 1], [2, 0], [1, 1], [1, 0], [0, 0]]

player = []
computer = []
stock = []
snake = []
player_to_move = None


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
        return None
    if player_double > computer_double:
        snake.append(player_double)
        player.remove(player_double)
        return "computer"
    snake.append(computer_double)
    computer.remove(computer_double)
    return "player"


while not player_to_move:
    deal_dominoes()
    player_to_move = find_starting_player()
print(f"Stock Pieces: {stock}")
print(f"Computer pieces: {computer}")
print(f"Player pieces: {player}")
print(f"Domino snake: {snake}")
print(f"Status: {player_to_move}")
