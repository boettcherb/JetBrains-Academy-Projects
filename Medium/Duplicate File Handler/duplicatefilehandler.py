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


def main():
    if len(sys.argv) == 1:
        print("Directory is not specified")
        return

    file_format = input("Enter the file format: ")

    print("\nSize sorting options:\n1. Descending\n2. Ascending")
    option = input("\nEnter a sorting option:\n")
    while option != "1" and option != "2":
        print("\nWrong Option\n")
        option = input("Enter a sorting option:\n")

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

    check = input("\nCheck for duplicates?\n")
    while check != "yes" and check != "no":
        print("\nWrong Option\n")
        check = input("Check for duplicates?\n")
    if check == "no":
        return

    files_found = [f for f in files_found if f.hash in File.duplicate_hashes]
    last_size = -1
    last_hash = None
    number = 1
    for file in files_found:
        if file.size != last_size:
            last_size = file.size
            print(f"\n{file.size} bytes")
        if file.hash != last_hash:
            last_hash = file.hash
            print(f"Hash: {file.hash}")
        print(f"{number}. {file.path}")
        number += 1


if __name__ == "__main__":
    main()
