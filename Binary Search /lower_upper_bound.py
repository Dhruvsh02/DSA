# implement lower bound 

def lower_bound(arr,x):
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

def main():
    arr = [1,2,3,3,5,8,8,10,10,11]
    x = 1
    result = lower_bound(arr,x)
    print(f"lower bound is : {result}")
if __name__ == "__main__":
    main()


# implementing uupper bound

def upper_bound(arr,x):
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

def main():
    arr = [1,2,3,3,5,8,8,10,10,11]
    x = 1
    result = upper_bound(arr,x)
    print(f"upper bound is : {result}")
if __name__ == "__main__":
    main()
