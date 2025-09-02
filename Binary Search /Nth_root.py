# # find the Nth root of an integer m

# # linear search apporach 

# def multiply(i,n):
#     result = 1
#     for _ in range(n):
#         result *= i
#     return result
# def nth_root(n,m):
#     for i in range(1,m+1):
#         power = multiply(i,n)
#         if power == m:
#             return i 
#         elif power > m:
#             break
#     return -1

# def main():
#     n = int(input("enter the value of n(root) : "))
#     m = int(input("enter the value of m(number) : "))
#     result = nth_root(n,m)
#     if result != -1:
#        print(f"the {n} root of an integer {m} is: {result}")
#     else:
#         print(f"no integer exist")
# if __name__ == "__main__":
#     main()


# optimal approach using binary search

def multiply(mid,m,n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= mid
            n = n-1
        else:
            mid *= mid
            n //= 2
    return result
# for i in range(1,m+1):
# ans = 1
# for i in range(n):
#    ans *= mid
# if ans > m: return 2
# if ans == m: return 1
# return 0 
def nth_root(n,m):
    low,high = 1,m
    while low <= high:
        mid = (low+high)//2
        power = multiply(mid,n)
        if power == m:
            return mid
        elif power < m:
            low = mid+1
        else:
            high = mid-1
    return -1

def main():
    n = int(input("enter the value of n(root) : "))
    m = int(input("enter the value of m(number) : "))
    result = nth_root(n,m)
    if result != -1:
       print(f"the {n} root of an integer {m} is: {result}")
    else:
        print(f"no integer exist")
if __name__ == "__main__":
    main()
