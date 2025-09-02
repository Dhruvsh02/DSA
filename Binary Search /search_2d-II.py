# search in a 2d matrix 
# where the row is sorted in a left to right and column is sorted in a top to bottom sequence 
# better approach beause binary search plus complete iterartion 
def bs(matrix,target):
    n = len(matrix)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if matrix[mid] == target:
            return mid
        elif matrix[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1
def search(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        ind = bs(matrix[i],target)
        if ind != -1:
            return (i,ind)
    return (-1,-1)
def main():
    matrix = [[1,4,7,11,15],[2,3,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 30 
    result = search(matrix,target)
    print(f"the element found in row,col here: {result}")
if __name__=="__main__":
    main()
# optimal approach only binary search not directly applying but eleminating 
# eliminating col and adding row will find the element 

def search_matrix(matrix,target):
    n = len(matrix)
    row = 0
    col= n-1
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return (row,col)
        elif matrix[row][col] < target:
            row+=1
        else:
            col-=1
    return (-1,-1)
def main():
    matrix = [[1,4,7,11,15],[2,3,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 14
    result = search(matrix,target)
    print(f"the element found in row,col here: {result}")
if __name__=="__main__":
    main()


