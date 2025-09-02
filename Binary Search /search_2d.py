# search in a 2D matrix 
# brute force approach 

def matrix(arr , target):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == target :
                return i,j
    return False
def main():
    arr = [[3,4,7,9],[12,13,16,18],[20,21,23,29]]
    target = 23 
    result = matrix(arr,target)
    print(f"found at index: {result}")
if __name__=="__main__":
    main()

# binary sesrch approach with loop : better approach 

def binary_search(arr,target):
    n = len(arr)
    low = 0 
    high = n-1
    while low <= high :
        mid = (low+high)//2
        if arr[mid] == target:
            return True
        elif mid > target:
            high = mid-1
        else:
            low = mid+1
    return False 
def matrix(arr,target):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        if arr[i][0] <= target and target<= arr[i][m-1]:
            return binary_search(arr[i],target)
    return False
def main():
    arr = [[3,4,7,9],[12,13,16,18],[20,21,23,29]]
    target = 23 
    result = matrix(arr,target)
    print(f"found at index: {result}")
if __name__=="__main__":
    main()


# optimal approach -> binary search in which trying to flatter the 2d array into 1d 

def matrix(arr,target):
    n = len(arr)
    m = len(arr[0])
    low , high = 0 , (n*m-1)
    while low <= high:
        mid = (low+high)//2
        row = mid//m
        col = mid%m
        if arr[row][col] == target:
            return row,col
        elif arr[row][col] < target:
            low = mid+1
        else:
            high = mid-1
    return False
def main():
    arr = [[3,4,7,9],[12,13,16,18],[20,21,23,29]]
    target = 23 
    result = matrix(arr,target)
    print(f"found at index: {result}")
if __name__=="__main__":
    main()