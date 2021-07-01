import sys
import os


def main():
    if len(sys.argv) == 1:
        print("Directory is not specified")
        return

    file_format = input("Enter the file format: ")

    print("Size sorting options:\n1. Descending\n2. Ascending")
    option = input("Enter a sorting option:\n")
    while option != "1" and option != "2":
        print("\nWrong Option\n")
        option = input("Enter a sorting option:\n")

    files_found = []
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            if file.endswith(file_format):
                path = os.path.join(root, file)
                size = os.path.getsize(path)
                files_found.append((size, path))

    last_size = -1
    for file in sorted(files_found, reverse=(option == "1")):
        if file[0] != last_size:
            last_size = file[0]
            print(f"\n{file[0]} bytes")
        print(file[1])


if __name__ == "__main__":
    main()
