# search insert position problem 
# need to insert an element in an array and to return the index where it can be stored 

def search_insert(arr,x):
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
    x = 12
    result = search_insert(arr,x)
    print(f"search insert postion is : {result}")
if __name__ == "__main__":
    main()