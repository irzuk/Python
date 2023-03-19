import numpy as np


class Matrix:
    def __init__(self, l):
        self.data = l
        if len(self.data) == 0:
            raise MatrixInitException('Empty matrix')
        for line in self.data:
            if len(line) != len(self.data[0]):
                raise MatrixInitException('Not all rows same size')
        self.size = [len(self.data), len(self.data[0])]

    def __str__(self):
        s = ''
        for line in self.data:
            s += str(line) + '\n'
        return s

    def __add__(self, other):
        try:
            if self.size[0] != other.size[0] or self.size[1] != other.size[1]:
                raise MatrixOperException(self, other, 'Add failed')
            res = [[0 for _ in range(self.size[0])] for _ in range(self.size[1])]
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    res[i][j] = self.data[i][j] + other.data[i][j]
            return Matrix(res)
        except MatrixOperException as e:
            print(e)
            return None


    def __matmul__(self, other):
        try:
            if self.size[1] != other.size[0]:
                raise MatrixOperException(self, other, 'Matmul failed')
            res = [[0 for _ in range(self.size[0])] for _ in range(other.size[1])]
            for i in range(self.size[0]):
                for j in range(other.size[1]):
                    for k in range(other.size[0]):
                        res[i][j] += self.data[i][k] * other.data[k][j]
            return Matrix(res)
        except MatrixOperException as e:
            print(e)
            return None


    def __mul__(self, other):
        try:
            if self.size[0] != other.size[0] or self.size[1] != other.size[1]:
                raise MatrixOperException(self, other, 'Mul failed')
            res = [[0 for _ in range(self.size[0])] for _ in range(self.size[1])]
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    res[i][j] = self.data[i][j] * other.data[i][j]
            return Matrix(res)
        except MatrixOperException as e:
            print(e)
            return None


class MatrixOperException(Exception):
    def __init__(self, l, r, text):
        self.text = text + ': Wrong dims, left: ' + str(l.size) + ', right: ' + str(r.size)

    def __str__(self):
        return self.text


class MatrixInitException(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

# test for Init exception
# m1 = Matrix([[1, 1, 1], [0, 0]])

# test for Operation exception
# m2 = Matrix([[1, 1], [0, 0]])
# m3 = Matrix([[1, 1], [0, 0], [1, 1]])
# m4 = m2 + m3

np.random.seed(0)
left = Matrix(np.random.randint(0, 10, (10, 10)))
right = Matrix(np.random.randint(0, 10, (10, 10)))

print(str(left))
print(str(right))

with open("./artifacts/easy/matrix+.txt", 'w') as f:
    f.write(str(left + right))

with open("./artifacts/easy/matrix*.txt", 'w') as f:
    f.write(str(left * right))

with open("./artifacts/easy/matrix@.txt", 'w') as f:
    f.write(str(left @ right))
