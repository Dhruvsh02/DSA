# majority element in an array(brute force approach)

def element(arr,n):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count+=1
        if count > n//2:
           return arr[i]
        
    return -1
def main():
    arr = [1,2,5,4,5,5,5,5]
    n = len(arr)
    result = element(arr,n)
    if result == -1:
        print("No majority element found")
    else:
        print("Majority element is:", result)
if __name__ == "__main__":
    main()

# better approach using hash map
def element(arr,n):
    ele_map = {}
    n = len(arr)
    for i in range(n):
        if arr[i] in ele_map:
            ele_map[arr[i]] +=1
        else:
            ele_map[arr[i]] = 1
    for i in ele_map:
        if ele_map[i] > n//2:
            return i
    return -1
def main():
    arr = [1,2,5,4,5,5,5,5]
    n = len(arr)
    result = element(arr,n)
    if result == -1:
        print("No majority element found")
    else:
        print("Majority element is:", result)
if __name__ == "__main__":
    main()

# optimal approach using moore's voting algorithm 
def element(arr,n,ele):
    count = 0
    for i in range(n):
        if count == 0:
            count = 1
            ele = arr[i]
        elif arr[i] == ele:
            count += 1
        else:
            count -= 1

    count1 = 0
    for i in range(n):
        if arr[i] == ele:
            count1 += 1
    if count1 > n//2:
        return ele
    return -1

def main(): 
    arr = [1,2,5,4,5,5,5,5]
    n = len(arr)
    ele = -1
    result = element(arr,n,ele)
    if result == -1:
        print("No majority element found")
    else:
        print("Majority element is:", result)
if __name__ == "__main__":
    main()
        
