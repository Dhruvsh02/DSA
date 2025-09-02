def insertion(key):
    n= len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
arr=[44,33,55,11,22,77]
sorted_arr= insertion(arr)
print(sorted_arr)