def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for x in matrix:
        x.reverse()
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))