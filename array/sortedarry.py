# check if the array is sorted or not 

def sorted_array(arr,n):
    for i in range(1,n):
        if arr[i] >= arr[i-1]:
            continue
        else:
            print("The array is not sorted")
            return False
    print("The array is sorted")
    return True

def main():
    arr=[2,5,6,8,19]
    n = len(arr)
    sorted_array(arr,n)
if __name__ == "__main__":
    main()