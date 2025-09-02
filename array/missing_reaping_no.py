# find the missing and repearting numbers 

# brute force approach 

def missing_repeating(arr):
    repeating = -1
    missing = -1
    n = len(arr)
    for i in range(1,n+1):
        count = 0
        for j in range(n):
            if arr[j] == i:
                count +=1
        if count == 2:
            repeating = i
        elif count == 0:
            missing = i
        if repeating != -1 and missing != -1:
           break
    return repeating , missing 

def main():
    arr = [4,2,3,6,1,1]
    result = missing_repeating(arr)
    print(f"repeating and missing : {result}")
if __name__ == "__main__":
    main()

# better approach using hasharr

def missing_repeating(arr):
    n = len(arr)
    missing , repeating = -1,-1
    hash_arr = [0] * (n+1)
    for i in range(n):
        hash_arr[arr[i]] +=1
    for i in range(1,n+1):
        if hash_arr[i] == 2:
            repeating = i
        elif hash_arr[i] == 0:
            missing = i
        if repeating != -1 and missing != -1:
            break 
    return missing , repeating

def main():
    arr = [4,2,3,6,1,1]
    result = missing_repeating(arr)
    print(f"repeating and missing : {result}")
if __name__ == "__main__":
    main()

# optimal approach 

def missing_repeating(arr):
    n = len(arr)
    x,y = -1,-1
    sn = (n * (n+1)) // 2
    s2n = (n * (n+1) * (2*n+1)) // 6 
    s = 0 
    s2 = 0
    for i in range(n):
        s += arr[i]
        s2 += arr[i] * arr[i]
    val1 = s-sn
    val2 = s2-s2n
    val2 = val2//val1
    x = (val1 + val2) // 2
    y = x - val1
    return x,y


def main():
    arr = [4,2,3,6,1,1]
    result = missing_repeating(arr)
    print(f"repeating and missing : {result}")
if __name__ == "__main__":
    main()

# optimal using xor

def missing_repeating(arr):
    n = len(arr)
    xr = 0 
    for i in range(n):
        xr = xr ^ arr[i]
        xr = xr ^ (i+1)
    bitno = 0
    while True:
        if xr & (1 << bitno):
            break
        bitno+=1
    zero = 0
    one = 0 
    for i in range(n):
        if arr[i] & (1 << bitno):
            one = one ^ arr[i]
        else:
            zero = zero ^ arr[i]
    for i in range(1,n+1):
        if i & (1 << bitno):
            one = one ^ i
        else:
            zero = zero ^ i
    count = arr.count(zero) 
    if count == 2:
        repeating = zero
        missing = one
    else:
        repeating = one
        missing = zero

    return repeating, missing
def main():
    arr = [4,2,3,6,1,1]
    result = missing_repeating(arr)
    print(f"repeating and missing : {result}")
if __name__ == "__main__":
    main()