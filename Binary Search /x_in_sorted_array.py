# binary search to find X in sorted array 
 
def binary_search(arr,target):
    n = len(arr)
    low = 0 
    high = n-1
    
    while low <= high : 
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    arr = [3,4,5,6,7,11,89,90]
    target = 89
    result = binary_search(arr,target)
    print(f"Element found at index: {result}")
if __name__ == "__main__":
    main()

# uusing recursion 

def binary_search(arr,target,low,high):

    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binary_search(arr,target,mid+1,high)
    else:
        return binary_search(arr,target,low,mid-1)
    

def main():
    arr = [3,4,5,6,7,11,89,90]
    target = 89
    result = binary_search(arr,target,0,len(arr)-1)
    print(f"Element found at index: {result}")
if __name__ == "__main__":
    main()

