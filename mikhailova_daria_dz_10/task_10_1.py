
class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return '|' + str(f'|\n|'.join([f'\t'.join([str(el) for el in _]) for _ in self.matrix_list])) + '|'

    def __add__(self, other):
        for i in range(len(self.matrix_list)):
            for p in range(len(other.matrix_list[i])):
                self.matrix_list[i][p] = self.matrix_list[i][p] + other.matrix_list[i][p]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
n = Matrix([[8, 9, 10], [10, 11, 12], [12, 13, -14]])
print(m.__add__(n))
