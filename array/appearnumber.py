# find the number that appears once in an array(brute force approach)

def appear_number_ones(arr):
    for i in range(len(arr)):
        num = arr[i]
        count = 0
    
        for j in range(len(arr)):
            if arr[j] == num:
                count += 1

        if count == 1:
            return num
    return -1

def main():
    arr = [2,2,3,3,4,4,5,5,5]
    result = appear_number_ones(arr)
    print("The number that appears once: ", result)
if __name__ == "__main__":
    main()

# better approach using hashing 

def appear_number_ones(arr):
    maxi = arr[0]
    for i in range(len(arr)):
        maxi = max(maxi, arr[i])
    hash = [0] * (maxi + 1)
    for i in range(len(arr)):
        hash[arr[i]] += 1
    for i in range(len(hash)):
        if hash[i] == 1:
            return i
    return -1

def main():
    arr = [1,1,2,2,3,3,4,4,5,5,5,6]
    result = appear_number_ones(arr)
    print("The number that appears once: ", result)
if __name__ == "__main__":
    main()


# optimal approach using XOR gate 
# XOR  assumes all other appears two times not more 

def appear_number_ones(arr):
   XOR  = 0
   for i in range(len(arr)):
       XOR = XOR ^ arr[i]
   
   return XOR

def main():
    arr = [1,1,2,2,4,4,5,5,6]
    result = appear_number_ones(arr)
    print("The number that appears once: ", result)
if __name__ == "__main__":
    main()
