def rotate(matrix):
    # allocate new matrix
    rotate_matrix = []

    for index in range(len(matrix)):
        rotate_matrix.append([])
        for e in matrix:
            rotate_matrix[index].append(e[index])
        rotate_matrix[index].reverse()
    return rotate_matrix

def new_rotate(matrix):
    # allocate new matrix with another way
    temp_matrix = [row[:] for row in matrix]
    size = len(matrix[0])

    for x in range(0,size):
        for j in range(0,size):
            temp_matrix[j][size-1-x] = matrix[x][j]
    return temp_matrix

print(new_rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))