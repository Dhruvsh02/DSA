# floor and ceil in sorted array 


def floor(arr,x):
    n = len(arr)
    low , high = 0, n-1
    ans = -1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] <= x:
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    return ans  

def ceil(arr,x):
    n = len(arr)
    low , high = 0, n-1
    ans = -1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] >= x:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans

def main():
    arr = [1,2,3,3,5,8,8,10,10,11]
    x = 4
    floor_result = floor(arr,x)
    ceil_result = ceil(arr,x)
    print(f"Floor of {x} is: {floor_result}")
    print(f"Ceil of {x} is: {ceil_result}")
if __name__ == "__main__":
    main()