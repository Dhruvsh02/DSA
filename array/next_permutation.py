# find next permutation of an array optimal approach

def permuatation(arr):
    index = -1
    n = len(arr)
    for i in range(n-2,0,-1):
        if arr[i] < arr[i+1]:
            index = i
            break
    if index == -1:
        arr.reverse()
        return arr
    for i in range(n-1,index,-1):
        if arr[i] > arr[index]:
            arr[i],arr[index] = arr[index],arr[i]
            break
    arr[index+1:] = reversed(arr[index+1:])   # reverse the array from index+1 to n-1
    return arr
def main(): 
    arr = [2,1,5,4,3,0,0]
    result = permuatation(arr)
    print("The next permutation is: ", result)
if __name__ == "__main__":
    main()
