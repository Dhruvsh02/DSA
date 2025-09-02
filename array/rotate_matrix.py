# brute force approach

def rotate_matrix(matrix):
    n = len(matrix)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[j][n-1-i] = matrix[i][j]
    return ans
def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    result = rotate_matrix(matrix)
    for row in result:
        print(row)
    print("The rotated matrix is: ")
if __name__ == "__main__":
    main()


# optimal approach  

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(0,n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    result = rotate_matrix(matrix)
    for row in result:
        print(row)
    print("The rotated matrix is: ")
if __name__ == "__main__":
    main()