# find out how many times array has been rorated 

def times_array_rotated(arr):
    low , high = 0 , len(arr) - 1
    ans = int(1e9)
    ind = -1
    while low < high:
        mid = (low+high)//2
        # Check if the array is already sorted
        # then always arr[low] will be the minimum in that search space 
        if arr[low] <= arr[high]:
            if arr[low] < ans:
              ind = low
              ans = arr[low]
            break
        if arr[low] <= arr[mid]:
            if arr[low] < ans:
              ind = low
              ans = arr[low] 
            low = mid + 1
        else:
            high = mid - 1
            if arr[mid] <= ans:
                ind = mid
                ans = arr[mid]
    return ind 
    
def main():
    arr = [3,4,5,1,2]
    print(times_array_rotated(arr)) 
if __name__ == "__main__":
    main()

