import math

def getCofactor(m, i, j):
    return [row[i:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

def det(A):
    # case 1: matrix is nonsquare; dont calculate det in this case
    if i != j:
        return "nonexistent for nonsquare matrices!"
    # case 2: matrix is larger than 2 by 2
    if len(A) != 2:
        res = 0
        # for loop traverses across every column of A
        for highlight_column in range(len(A)):
            sign = (-1) ** highlight_column
            sub_det = det(getCofactor(A, 0, highlight_column))
            res += (sign * A[0][highlight_column] * sub_det)
        return res
    # case 3: matrix is 2 by 2; we just use cross multiplication row and gg
    res = A[0][0] * A[1][1] - A[1][0] * A[0][1]
    return res


# =========User Matrix Input=====================

r = int(input("Enter the number of rows you want:"))
c = int(input("Enter the number of columns you want:"))

mat = []
print("Enter the entries here row-wise; entries wrap to the next row after the row is filled: ")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    mat.append(a)
# print user input matrix
for i in range(r):
    for j in range(c):
        print(mat[i][j], end=" ")
    print()

print('The Determinant of the matrix is: ', det(mat))
