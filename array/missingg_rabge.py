# missing range leeetcode 163 

def missingRange(nums, lower, upper):
    n = len(nums)
    result = []
    prev = lower - 1
    for i in range(n+1):
        curr = nums[i] if i < n else upper + 1
        if curr - prev > 1:
            result.append(f"{prev + 1},{curr - 1}" if curr - prev > 2 else str(prev + 1))
        prev = curr
    return result

def main():
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(missingRange(nums, lower, upper))

if __name__ == "__main__":
    main()