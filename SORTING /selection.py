def selection(arr):
    
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index]= arr[min_index],arr[1]

    return arr
arr= [44,33,55,11,22,77]
sorted_arr = selection(arr)
print(sorted_arr)    
    

