# find the first oe last occurrence of an element in a sorted array

# brute force approach using linear search

def first_last_occur(arr, target):
    n = len(arr)
    first,last = -1,-1
    for i in range(n):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    return first, last

def main():
    arr = [1,2,3,3,5,8,8,10,10,11]
    target = 3
    result = first_last_occur(arr, target)
    print(f"first and last occurrence of {target} are: {result}")
if __name__ == "__main__":
    main()

# optimal approach using binary search using lower and upper bound

# implement lower bound 

def first_occurance(arr,x):
    n = len(arr)
    low = 0 
    high = n-1
    ans = n
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= x:
            ans = mid
            high = mid-1
        else:
            low = mid+1 
    return ans 

def last_occurance(arr,x):
    n = len(arr)
    low = 0 
    high = n-1
    ans = n
    while low <= high:
        mid = (low + high)//2
        if arr[mid] > x:
            ans = mid
            high = mid-1
        else:
            low = mid+1 
    return ans 
def occurance(arr,x):
    n = len(arr)
    first = first_occurance(arr, x)
    last = last_occurance(arr, x)
    if first == n or arr[first] != x:
        return -1, -1  # Element not found
    return first, last-1

def main():
    arr = [1,2,3,3,5,8,8,10,10,11]
    x = 8
    result = occurance(arr, x)
    print(f"First and last occurrence of {x} are: {result}")

if __name__ == "__main__":
    main()

# using normal binary search method 

def first_occur(arr,x):
    n = len(arr)
    low , high = 0,n-1
    first = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            first = mid
            high = mid-1
        elif arr[mid] < x:
            low = mid + 1
        else: 
            high = mid - 1
    return first

def last_occur(arr,x):  
    n = len(arr)
    low , high = 0,n-1
    last = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else: 
            high = mid - 1
    return last
def occurance(arr,x):
    first = first_occur(arr, x)
    last = last_occur(arr, x)
    if first == -1 or last == -1:
        return -1, -1  # Element not found
    return first, last
def counnt_occurrence(arr, x):
    first, last = occurance(arr, x)
    if first == -1:
        return 0  # Element not found
    return last - first + 1  # Count of occurrences
def main():
    arr = [1,2,3,3,5,8,8,10,10,11]
    x = 8
    result = occurance(arr, x)
    result_count = counnt_occurrence(arr, x)
    print(f"Count of occurrences of {x} is: {result_count}")
    print(f"First and last occurrence of {x} are: {result}")
if __name__ == "__main__":
    main()
                