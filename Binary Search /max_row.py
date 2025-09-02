# row with maximum numbers of 1s 

def matrixx(arr):
    n = len(arr)
    m = len(arr[0])
    ind , max_count = -1,-1
    for i in range(n):
        count_row = 0
        for j in range(m):
            count_row += arr[i][j]
        if count_row > max_count:
            max_count = count_row
            ind = i

    return ind , max_count

def main():
    arr = [[0,0,1,1,1],[0,0,0,0,0],[0,1,1,1,1],[0,0,0,0,0],[0,1,1,1,1]]
    result = matrixx(arr)
    print(f"row with maximum number of 1s:{result}")
if __name__=="__main__":
    main()


# binary approach using lower bound 

def lower_bount(arr,n,x):
    low , high = 0 ,n-1
    ans = n
    while low <= high :
        mid = (low+high)//2
        if arr[mid] >= x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans 
def row_max(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count_max = -1
    ind = -1
    for i in range(n):
        count_ones = m - lower_bount(matrix[i], m, 1)
        if count_ones > count_max:
            count_max= count_ones
            ind = i

    return ind , count_max
def main():
    arr = [[0,0,1,1,1],[0,0,0,0,0],[0,1,1,1,1],[0,0,0,0,0],[0,1,1,1,1]]
    result = row_max(arr)
    print(f"row with maximum number of 1s:{result}")
if __name__=="__main__":
    main()
