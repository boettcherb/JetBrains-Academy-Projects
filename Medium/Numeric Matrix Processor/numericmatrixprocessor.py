class Matrix:
    def __init__(self, rows, cols, matrix=None):
        self.rows = rows
        self.cols = cols
        if matrix is None:
            self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            self.matrix = matrix

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return None
        new_matrix = Matrix(self.rows, self.cols, self.matrix[:])
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix[i][j] += other[i][j]
        return new_matrix

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_matrix = Matrix(self.rows, self.cols, self.matrix[:])
            for row in new_matrix:
                for j in range(self.cols):
                    row[j] *= other
            return new_matrix
        else:
            if self.cols != other.rows:
                return None
            new_matrix = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        new_matrix[i][j] += self[i][k] * other[k][
                            j]
            return new_matrix

    def transpose(self, option):
        if option == 1:
            new_matrix = Matrix(self.cols, self.rows)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix[j][i] = self[i][j]
            return new_matrix
        if option == 2:
            new_matrix = Matrix(self.cols, self.rows)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_row = self.cols - j - 1
                    new_col = self.rows - i - 1
                    new_matrix[new_row][new_col] = self[i][j]
            return new_matrix
        if option == 3:
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.cols):
                for j in range(self.rows):
                    new_matrix[i][j] = self[i][self.cols - j - 1]
            return new_matrix
        if option == 4:
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.cols):
                for j in range(self.rows):
                    new_matrix[i][j] = self[self.rows - i - 1][j]
            return new_matrix

    def determinant(self):
        if self.rows != self.cols:
            return None
        if self.rows == 1:
            return self[0][0]
        if self.rows == 2:
            return self[0][0] * self[1][1] - self[1][0] * self[0][1]
        determinant = 0
        for i in range(self.rows):
            cofactor = self.cofactor(0, i)
            sign = -1 if i % 2 else 1
            determinant += sign * self[0][i] * cofactor.determinant()
        return determinant

    def cofactor(self, row, col):
        matrix_copy = [row.copy() for row in self.matrix]
        del matrix_copy[row]
        for i in range(self.rows - 1):
            del matrix_copy[i][col]
        return Matrix(self.rows - 1, self.rows - 1, matrix_copy)

    def __str__(self):
        string = ""
        for row in self.matrix:
            string += " ".join(str(num) for num in row) + "\n"
        return string


def get_matrix(size_prompt, matrix_prompt):
    matrix = []
    rows, cols = (int(a) for a in input(size_prompt).split())
    print(matrix_prompt)
    for _ in range(rows):
        user_input = input().split()
        try:
            row = [int(a) for a in user_input]
            matrix.append(row)
        except ValueError:
            row = [float(a) for a in user_input]
            matrix.append(row)
    return Matrix(rows, cols, matrix)


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("0. Exit")
        choice = int(input("Your choice: "))
        res = None
        if choice == 0:
            break
        if choice == 1:
            a = get_matrix("Enter size of first matrix: ",
                           "Enter first matrix:")
            b = get_matrix("Enter size of second matrix: ",
                           "Enter second matrix:")
            res = a + b
        elif choice == 2:
            a = get_matrix("Enter size of matrix: ", "Enter matrix:")
            s = input("Enter constant: ")
            scalar = int(s) if s.isdecimal() else float(s)
            res = a * scalar
        elif choice == 3:
            a = get_matrix("Enter size of first matrix: ",
                           "Enter first matrix:")
            b = get_matrix("Enter size of second matrix: ",
                           "Enter second matrix:")
            res = a * b
        elif choice == 4:
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            option = int(input("Your choice: "))
            a = get_matrix("Enter matrix size: ", "Enter matrix:")
            res = a.transpose(option)
        elif choice == 5:
            a = get_matrix("Enter size of matrix: ", "Enter matrix:")
            res = a.determinant()
        if res is None:
            print("The operation could not be performed")
        else:
            print("The result is:")
            print(res)


if __name__ == "__main__":
    main()
