m = [
    [1, 1, 0, 0],
    [2, -1, 3, 3],
    [1, -2, -1, 0]
]


def first(row):
    '''returns index of first non-zero item, none if there are none'''
    for i, element in enumerate(row):
        if element != 0:
            return i


def row_mult(row, constant):
    for i, element in enumerate(row):
        row[i] = element * constant


def add_mult(row, other_row, constant):
    for i, element in enumerate(row):
        row[i] = other_row[i] * constant


def gauss(mat: list):
    if not mat:
        return mat
    for i in range(len(mat[0])):
        for k, row in enumerate(mat):
            if row[i]:
                index = first(row)
                row_mult(row, 1 / row[index])
                for j, other_row in enumerate(mat):
                    if j != i:
                        add_mult(other_row, row, -other_row[index])
                mat.pop(k)
                return row + [gauss(mat)]


print(gauss(m))