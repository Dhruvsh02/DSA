# leaders in an array ( using brute force approach)

def leader_array(arr):
    ans = []
    n = len(arr)
    for i in range(n):
        leader = True
        for j  in range(i+1,n):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader == True:
            ans.append(arr[i])
    return ans

def main():
    arr = [16,17,4,3,5,2]
    result = leader_array(arr)
    print("The leaders in the array are: ", result)
if __name__ == "__main__":
    main()

# optimal approach

def leader_array(arr):
    n = len(arr)
    ans = []
    maxi = -1
    for i  in range(n-1,-1,-1):   # traversing from right to left
        if arr[i] > maxi:
            ans.append(arr[i])
            maxi = arr[i]
        maxi = max(maxi,arr[i])
    return ans
def main():
    arr = [16,17,4,3,5,2]
    result = leader_array(arr)
    print("The leaders in the array are: ", result)
if __name__ == "__main__":
    main()