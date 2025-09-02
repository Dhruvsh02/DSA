# K th missing positive number
# brute force solution

def find_kth_missing(arr, k):
    n = len(arr)
    for i in range(n):
        if arr[i] <= k:
            k+=1
        else:
            break
    return k
def main():
    arr = [2, 3, 4, 7, 11]
    k = 5
    result = find_kth_missing(arr, k)
    print(f"The {k}th missing positive number is: {result}")    
if __name__ =="__main__":
    main()

# binary search solution

def find_kth_missing(arr, k):
    low,high = 0, len(arr) - 1
    missing_count = 0 
    while low <= high:
        mid = (low+high)//2
        missing_count = arr[mid] - (mid+1)
        if missing_count < k:
            low = mid+1
        else:
            high = mid - 1
    return low + k   # return high + 1 + k because moe = k-misdsing_count
def main():
    arr = [2, 3, 4, 7, 11]
    k = 5
    result = find_kth_missing(arr, k)
    print(f"The {k}th missing positive number is: {result}")
if __name__ =="__main__":
    main() 
