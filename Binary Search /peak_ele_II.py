# find peak element - II
# means that 4 adjacent are not samee 
# up down left right
def max_element(mat,n,m,col):
    maxvalue = -1
    index = -1
    for i in range(n):
        if mat[i][col] > maxvalue:
            maxvalue = mat[i][col]
            index = i
    return index
def function(mat):
    n = len(mat)
    m = len(mat[0])
    low , high = 0 , m-1
    while low <= high :
        mid = (low+high)//2
        row = max_element(mat,n,m,mid)

        left = mat[row][mid-1] if mid-1 >=0 else -1
        right = mat[row][mid+1] if mid+1 < m else -1

        if mat[row][mid] > left and mat[row][mid] > right:
            return (row,mid)
        elif mat[row][mid] < left:
            high = mid-1
        else: 
            low = mid+1
    return (-1,-1)
def main():
    mat = [[4,5,5,1,4,5],[2,9,3,2,3,2],[1,7,6,0,1,3],[3,6,2,3,7,2]]
    result = function(mat)
    print(f"peak element in matrix is :{result},value = {mat[result[0]][result[1]]}")
if __name__ == "__main__":
    main()