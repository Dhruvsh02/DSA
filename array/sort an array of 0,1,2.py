# This code sorts an array containing only 0s, 1s, and 2s in a single pass.(using better approach)

def sort(arr,n):
    n = len(arr)
    count0=0
    count1=0
    count2=0
    for i in range(n):
        if arr[i]==0:
            count0+=1
        elif arr[i]==1:
            count1+=1
        else:
            count2+=1
    for i in range(count0):
        arr[i] = 0
    for i in range(count0,count0+count1):
        arr[i] = 1
    for i in range(count0+count1,n):
        arr[i] = 2
    return arr

def main():
    arr = [0,1,2,0,1,2,0,1,2]
    n = len(arr)
    result = sort(arr,n)
    print("Sorted array is:", result)
if __name__ == "__main__":
    main()

# now using dutch national flag algorithm(optimal approach)

# a[mid] == 0
# # swap a[low] and a[mid]
# # increment low and mid

# a[mid] == 1
# # increment mid

# a[mid] == 2
# # swap a[mid] and a[high]
# # decrement high

def sort(arr,n):
    low = 0
    mid = 0
    high = n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low +=1
            mid += 1
        elif arr[mid] == 1:
            mid +=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -=1
    return arr

def main():
    arr = [0,1,2,0,1,2,0,1,2]
    n = len(arr)
    result = sort(arr,n)
    print("Sorted array is:", result)
if __name__ == "__main__":
    main()