# brute force approaach 

def set_matrix_zeros(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                mark_row(matrix, i)
                mark_col(matrix, j)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix
def mark_row(matrix, row):
    n = len(matrix[0])
    for j in range(n):
        if matrix[row][j] != 0:
            matrix[row][j] = -1
def mark_col(matrix, col):
    n = len(matrix)
    for i in range(n):
        if matrix[i][col] != 0:
            matrix[i][col] = -1
def main():
    matrix = [[1, 1, 0, 1],
              [1, 1, 1, 1],
              [0, 1, 1, 1],
              [1, 1, 1, 1]]
    result = set_matrix_zeros(matrix)
    print("The matrix after setting zeros is: ")
    for row in result:
        print(row)
if __name__ == "__main__":
    main()

# better approach       

def set_matrix_zeros(matrix):
    n = len(matrix)
    m = len(matrix[0])
    row = [0] * n
    col = [0] * m
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]: 
                matrix[i][j] = 0
                
    return matrix
def main():
    matrix = [[1, 1, 0, 1],
              [1, 1, 1, 1],
              [0, 1, 1, 1],
              [1, 1, 1, 1]]
    result = set_matrix_zeros(matrix)
    print("The matrix after setting zeros is: ")
    for row in result:
        print(row)
if __name__ == "__main__":
    main()

# optimal approach

def set_matrix_zeros(matrix):
    n = len(matrix)
    m = len(matrix[0])
    col0 = 1 
    for i in range(n):
        for j in range(m):
            if matrix[i][j] ==0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0
    return matrix 
def main():
    matrix = [[1, 1, 0, 1],
              [1, 1, 1, 1],
              [0, 1, 1, 1],
              [1, 1, 1, 1]]
    result = set_matrix_zeros(matrix)
    print("The matrix after setting zeros is: ")
    for row in result:
        print(row)
if __name__ == "__main__":
    main()

     