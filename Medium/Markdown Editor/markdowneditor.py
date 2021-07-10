formatters = ["plain", "bold", "italic", "header", "link", "inline-code", 
              "ordered-list", "unordered-list", "new-line"]
special = ["!done", "!help"]


def get_input():
    global formatters
    while True:
        user_input = input("Choose a formatter: ")
        if user_input in formatters or user_input in special:
            return user_input
        print("Unknown formatting type or command")


while True:
    user_formatter = get_input()
    if user_formatter == "!done":
        break
    if user_formatter == "!help":
        print("Available formatters:", *formatters)
        print("Special commands:", *special)
