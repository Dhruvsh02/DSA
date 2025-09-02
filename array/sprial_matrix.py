def sprial_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    top, bottom, left, right = 0, n - 1, 0, m - 1
    result = [] 
    while top <= bottom or left <= right:
     for i in range(left,right+1):
        result.append(matrix[top][i])
     top += 1
     for i in range(top,bottom+1):
        result.append(matrix[i][right])
     right -= 1
     if top <= bottom :
      for i in range(left,right-1,-1):
        result.append(matrix[bottom][i])
     bottom -= 1
     if left <= right:
      for i in range(bottom,top-1,-1):
        result.append(matrix[i][left])
     left += 1
    return result

def main():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    result = sprial_matrix(matrix)
    print("The spiral order of the matrix is: ", result)
if __name__ == "__main__":
    main()





