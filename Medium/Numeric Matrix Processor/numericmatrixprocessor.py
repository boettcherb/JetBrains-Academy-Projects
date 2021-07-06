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
                new_matrix[i][j] += other.matrix[i][j]
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
                        new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return new_matrix

    def transpose(self, option):
        if option == 1:
            new_matrix = Matrix(self.cols, self.rows)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.matrix[j][i] = self.matrix[i][j]
            return new_matrix
        if option == 2:
            new_matrix = Matrix(self.cols, self.rows)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_row = self.cols - j - 1
                    new_col = self.rows - i - 1
                    new_matrix.matrix[new_row][new_col] = self.matrix[i][j]
            return new_matrix
        if option == 3:
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.cols):
                for j in range(self.rows):
                    new_matrix.matrix[i][j] = self.matrix[i][self.cols - j - 1]
            return new_matrix
        if option == 4:
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.cols):
                for j in range(self.rows):
                    new_matrix.matrix[i][j] = self.matrix[self.rows - i - 1][j]
            return new_matrix
    
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
        uip = input().split()
        matrix.append([int(a) if a.isdecimal() else float(a) for a in uip])
    return Matrix(rows, cols, matrix)


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("0. Exit")
        choice = int(input("Your choice: "))
        res = None
        if choice == 0:
            break
        if choice == 1:
            a = get_matrix("Enter size of first matrix: ", "Enter first matrix:")
            b = get_matrix("Enter size of second matrix: ", "Enter second matrix:")
            res = a + b
        elif choice == 2:
            a = get_matrix("Enter size of matrix: ", "Enter matrix:")
            s = input("Enter constant: ")
            scalar = int(s) if s.isdecimal() else float(s)
            res = a * scalar
        elif choice == 3:
            a = get_matrix("Enter size of first matrix: ", "Enter first matrix:")
            b = get_matrix("Enter size of second matrix: ", "Enter second matrix:")
            res = a * b
        elif choice == 4:
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            option = int(input("Your choice: "))
            a = get_matrix("Enter matrix size: ", "Enter matrix:")
            res = a.transpose(option)
        if res == None:
            print("The operation could not be performed")
        else:
            print("The result is:")
            print(res)

if __name__ == "__main__":
    main()
