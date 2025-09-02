# peak element in an array
# brute force approach using linear search 

def peak_elemewnt(arr):
    n = len(arr)
    for i in range(n):
        if ((i == 0 or arr[i-1] < arr[i] ) and (i==n-1 or arr[i] > arr[i+1] )):
            return arr[i]
    return -1
def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(peak_elemewnt(arr))
if __name__ == "__main__":
    main()


# optimal approach using binary search

def peak_element_binary(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[1]
    if arr[n-1] > arr[n-2]:
        return arr[n-1]
    low , high = 1 , n-2
    while low <= high:
        mid = (low + high)//2
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return arr[mid]
        elif arr[mid] > arr[mid-1]:
            low = mid + 1
        elif arr[mid] > arr[mid+1]:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1

def main():
    arr = [1,2,3,4,5,6,4,5,3]
    print(peak_element_binary(arr))
if __name__ == "__main__":
    main()