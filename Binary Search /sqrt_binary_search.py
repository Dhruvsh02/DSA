# finding the square root of a number using binary search 

# using lenear search to find the square root of a number is not efficient, especially for large numbers.

def sqrt_binary_search(n):
    if n < 0:
        raise ValueError("Cannot compute square root of negative number")
    if n == 0 or n == 1:
        return n
    ans = 1
    for i in range(1,n+1):
        if i * i <= n:
            ans = i
        else:
            break

    return ans
def main():
    n = int(input("Enter a number to find its square root: "))
    result = sqrt_binary_search(n)
    print(f"The square root of {n} is approximately {result}")
if __name__ == "__main__":
    main()

# using binary search to find the square root of a number is more efficient than linear search, especially for large numbers.

def sqrt_binary_search(n):
    if n < 0:
        raise ValueError("Cannot compute square root of negative number")
    if n == 0 or n == 1:
        return n
    low,high = 1,n
    ans = 1
    while low <= high:
        mid = (low+high)//2
        if mid*mid <= n:
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return ans
def main():
    n = int(input("Enter a number to find its square root: "))
    result = sqrt_binary_search(n)
    print(f"The square root of {n} is approximately {result}")
if __name__ == "__main__":
    main()