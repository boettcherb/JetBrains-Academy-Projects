def get_formatter(formatters, special):
    while True:
        user_input = input("Choose a formatter: ")
        if user_input in formatters or user_input in special:
            return user_input
        print("Unknown formatting type or command")


def plain():
    return input("Text: ")


def bold():
    return f"**{input('Text: ')}**"


def italic():
    return f"*{input('Text: ')}*"


def header():
    level = int(input("Level: "))
    while level < 1 or level > 6:
        print("The level should be within the range of 1 to 6")
        level = int(input("Level: "))
    text = input("Text: ")
    return f"{'#' * level} {text}\n"


def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def inline_code():
    return f"`{input('Text: ')}`"


def new_line():
    return "\n"


def md_list(formatter):
    num_rows = int(input("Number of rows: "))
    while num_rows < 1:
        print("The number of rows should be greater than zero")
        num_rows = int(input("Number of Rows: "))
    row = 1
    markdown = ""
    while row <= num_rows:
        md_symbol = str(row) + "." if formatter == "ordered-list" else "*"
        markdown += f"{md_symbol} {input(f'Row #{row}: ')}\n"
        row += 1
    return markdown


def main():
    formatters = ["plain", "bold", "italic", "header", "link", "inline-code",
                  "new-line", "ordered-list", "unordered-list"]
    special = ["!done", "!help"]
    functions = {"plain": plain, "bold": bold, "italic": italic,
                 "header": header, "link": link, "inline-code": inline_code,
                 "new-line": new_line, "ordered-list": md_list,
                 "unordered-list": md_list}
    markdown = ""
    while True:
        user_formatter = get_formatter(formatters, special)
        if user_formatter == "!done":
            break
        elif user_formatter == "!help":
            print("Available formatters:", *formatters)
            print("Special commands:", *special)
        else:
            if user_formatter in ("ordered-list", "unordered-list"):
                markdown += functions[user_formatter](user_formatter)
            else:
                markdown += functions[user_formatter]()
        print(markdown)
    with open("output.md", "w") as file:
        print(markdown, file=file, end="")


if __name__ == "__main__":
    main()
