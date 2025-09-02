# find missing number in array (brute force approach)

def missing(arr, n):
    for i in range(n+1):
        flag = 0 
        for j in range(n):
            if arr[j] == i:
                flag =1
                break
        if flag == 0:
            return i
def main():
    arr = [0,1,2,3,4,6,7,8]
    n = len(arr)
    result = missing(arr, n)
    print("The missing number is: ", result)
if __name__ == "__main__":
    main()


# optimal approach with using XOR gate 
def missing_number(arr, n):
    XOR1 = 0 
    XOR2 = 0
    for i in range(n):
        XOR1 = XOR1 ^ i
    for i in range(0,n-1):
        XOR2 = XOR2 ^ arr[i]
    return XOR1 ^ XOR2
def main():
    arr = [0,1,2,3,4,6,7,8]
    n = len(arr)
    result = missing_number(arr, n)
    print("The missing number is: ", result)
   
if __name__ == "__main__":
    main()


# optimal approach with using sum formula


def missing_number(arr, n):
    total = (n * (n - 1)) // 2
    sum1 = 0
    for i in range(n - 1):
        sum1 += arr[i]
    return total - sum1

def main():
    arr = [0, 1, 2, 3, 4, 6, 7, 8]
    n = len(arr)   # Corrected here
    result = missing_number(arr, n)
    print("The missing number is:", result)

if __name__ == "__main__":
    main()

