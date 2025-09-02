# This program finds the largest element in an array

def array():
    arr= [1, 2, 3, 4, 5]
    largest = arr[0]
    for i in range(len(arr)): # iterate through the array
        # check if the current element is greater than the largest
        if arr[i]>largest:   # if so, update largest
            largest = arr[i]   # update largest
    print("The largest element is:", largest)
    return largest
if __name__ == "__main__":
    array()