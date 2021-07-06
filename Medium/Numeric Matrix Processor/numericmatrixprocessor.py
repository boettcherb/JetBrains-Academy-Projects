class Matrix:
    def __init__(self, rows, cols, matrix):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return "ERROR"
        new_matrix = Matrix(self.rows, self.cols, self.matrix[:])
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix[i][j] += other.matrix[i][j]
        return new_matrix

    def __mul__(self, scalar):
        new_matrix = Matrix(self.rows, self.cols, self.matrix[:])
        for row in new_matrix:
            for j in range(self.cols):
                row[j] *= scalar
        return new_matrix

    def __str__(self):
        string = ""
        for row in self.matrix:
            string += " ".join(str(num) for num in row) + "\n"
        return string


def get_matrix_from_user():
    matrix = []
    rows, cols = [int(a) for a in input().split()]
    for _ in range(rows):
        matrix.append([int(a) for a in input().split()])
    return Matrix(rows, cols, matrix)


def main():
    a = get_matrix_from_user()
    scalar = int(input())
    print(a * scalar)


if __name__ == "__main__":
    main()
