# maximum product subarray
# brute force approach 

def max_prod_subarray(arr):
    n = len(arr)
    maxi = -1
    for i in range(n):
        for j in range(i,n):
            product = 1
            for k in range(i,j):
                product *= arr[k]
            maxi = max(maxi,product)
        return maxi

def main():
    arr = [2,3,-2,4]
    result = max_prod_subarray(arr)
    print("The maximum subarray sum is: ", result)
if __name__ == "__main__":
    main()


# better approach 

def max_prod_subarray(arr):
    n = len(arr)
    maxi = -1
    for i in range(n):
        product = 1
        for j in range(i,n):
            product *= arr[j]
            maxi = max(maxi,product)
        return maxi

def main():
    arr = [2,3,-2,4]
    result = max_prod_subarray(arr)
    print("The maximum subarray sum is: ", result)
if __name__ == "__main__":
    main()

# optimal approach using prefix and suffix 

def max_prod_subarray(arr):
    n = len(arr)
    maxi = -1
    prefix = 1
    suffix = 1
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix = prefix * arr[i]
        suffix *= arr[n-i-1]
        maxi = max(maxi,max(prefix,suffix))
    return maxi  

def main():
    arr = [2,3,-2,4]
    result = max_prod_subarray(arr)
    print("The maximum subarray sum is: ", result)
if __name__ == "__main__":
    main()