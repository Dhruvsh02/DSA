def search(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i 
    return -1

def main():
    arr=[1,2,3,4,5,7,8]
    num=5
    index=search(arr,num)
    print("element found at index",index)
if __name__ == "__main__":
    main()