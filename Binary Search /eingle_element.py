# single elemnt in a sorted array
# brute force approach  
# linear search

def single_element(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    for i in range(n):
        if i == 0:
            if arr[i] != arr[i+1]:
                return arr[i]
            elif i == n-1:
                if arr[i] != arr[i-1]:
                    return arr[i]
            else:
                if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
                    return arr[i]
    return arr[i]
def main():
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 5 ,5,6]
    print(single_element(arr))
if __name__ == "__main__":
    main()

# optimal approach
# using binary search

def single_element_binary(arr):
    n = len(arr)
    if n ==1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:    
        return arr[n-1]
    low , high = 1, n-1
    while low < high:
        mid = (low + high)//2
        if arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]:
            return arr[mid]
        if (mid % 2 ==1 and arr[mid-1] == arr[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    arr = [1, 1, 2, 2, 3, 4, 4, 5 ,5]
    print(single_element_binary(arr))
if __name__ == "__main__":
    main()
      