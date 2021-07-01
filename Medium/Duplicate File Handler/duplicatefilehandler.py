import sys
import os
import hashlib


class File:
    all_hashes = set()
    duplicate_hashes = set()

    def __init__(self, path, size):
        self.path = path
        self.size = size
        self.hash = self.get_hash_code()

    def sort_by_size(self):
        return self.size

    def get_hash_code(self):
        hash_object = hashlib.md5()
        with open(self.path, "rb") as f:
            for line in f:
                hash_object.update(line)
        code = hash_object.hexdigest()
        if code in File.all_hashes:
            File.duplicate_hashes.add(code)
        else:
            File.all_hashes.add(code)
        return code


def get_answer(prompt, a1, a2):
    print()
    answer = input(prompt)
    while answer != a1 and answer != a2:
        print("\nWrong option\n")
        answer = input(prompt)
    return answer


def get_numbers_to_delete(number):
    while True:
        try:
            numbers = []
            user_input = input("\nEnter file numbers to delete:\n")
            if user_input != "":
                for num in user_input.split():
                    numbers.append(int(num))
                if len([n for n in numbers if n < 1 or n > number]) == 0:
                    return numbers
            print("\nWrong Format")
        except ValueError:
            print("\nWrong Format")


def main():
    if len(sys.argv) == 1:
        print("Directory is not specified")
        return

    file_format = input("Enter the file format: ")
    print("\nSize sorting options:\n1. Descending\n2. Ascending")
    option = get_answer("Enter a sorting option:\n", "1", "2")

    files_found = []
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            if file_format == "" or file.endswith("." + file_format):
                path = os.path.join(root, file)
                size = os.path.getsize(path)
                files_found.append(File(path, size))
    files_found.sort(key=File.sort_by_size, reverse=(option == "1"))

    last_size = -1
    for file in files_found:
        if file.size != last_size:
            last_size = file.size
            print(f"\n{file.size} bytes")
        print(file.path)

    if get_answer("Check for duplicates?\n", "yes", "no") == "no":
        return 0
    files_found = [f for f in files_found if f.hash in File.duplicate_hashes]
    last_size = -1
    last_hash = None
    number = 0
    for file in files_found:
        if file.size != last_size:
            last_size = file.size
            print(f"\n{file.size} bytes")
        if file.hash != last_hash:
            last_hash = file.hash
            print(f"Hash: {file.hash}")
        number += 1
        print(f"{number}. {file.path}")

    if get_answer("Delete duplicate files?\n", "yes", "no") == "no":
        return 0
    numbers = get_numbers_to_delete(number)
    bytes_deleted = 0
    for num in numbers:
        bytes_deleted += files_found[num - 1].size
        os.remove(files_found[num - 1].path)
    print(f"\nTotal freed up space: {bytes_deleted}")


if __name__ == "__main__":
    main()
