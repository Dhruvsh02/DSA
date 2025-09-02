# rearrange array elements by sign 
# brute force app


def rearrange_array(arr):
    pos = []
    neg = []
    n = len(arr)
    for i in range(n):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])

    for i in range(n//2):
        arr[2*i] = pos[i]
        arr[2*i+1] = neg[i]
    return arr
def main():
    arr = [1,2,3,-4,-5,-6]
    result = rearrange_array(arr)
    print("The rearranged array is: ", result)
if __name__ == "__main__":
    main()


# using optimal approach

def rearrange_array(arr):
    n = len(arr)
    ans=[0]*n
    pos_index = 0
    neg_index = 1
    for i in range(n):
        if arr[i] < 0:
            ans[neg_index] = arr[i]
            neg_index += 2
        else:
            ans[pos_index] = arr[i]
            pos_index += 2 
    return ans

def main():
    arr = [1,2,3,-4,-5,-6]
    result = rearrange_array(arr)
    print("The rearranged array is: ", result)
if __name__ == "__main__":
    main()

# where positive and negitive is nor equal 

def rearrange_array(arr):
    pos = []
    neg = []
    n = len(arr)
    for i in range(n):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        index = len(neg) * 2 
        for i in range(len(neg),len(pos)):
            arr[index] = pos[i]
            index += 1
    else:
        for i in range(len(pos)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        index = len(pos) * 2 
        for i in range(len(pos),len(neg)):
            arr[index] = neg[i]
            index += 1
    return arr
def main():
    arr = [1,2,3,-4,-5,-6,8,9]
    result = rearrange_array(arr)
    print("The rearranged array is: ", result)
if __name__ == "__main__":
    main()