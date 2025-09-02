# majority element (n / 3 times)

# brute force solution

def majority_element(nums):
    n = len(nums)
    ls = []
    for i in range(n):
        if nums[i] not in ls:
            count = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1
            if count > n // 3:
                ls.append(nums[i])
    return ls

def main():
    nums = [1, 2, 3, 1, 1, 2, 1,2,2]
    print(majority_element(nums))
if __name__ == "__main__":
    main()


# better solution using hashing 

def majority_element(nums):
    n = len(nums)
    result = []
    count_map = {}
    min = n // 3 + 1
    for i in range(n):
        count_map[nums[i]] = count_map.get(nums[i] , 0 )+ 1
        if count_map[nums[i]] == min:
            result.append(nums[i])
    return result
def main():
    nums = [1, 2, 3, 1, 1, 2, 1, 2, 2]
    print(majority_element(nums))
if __name__ == "__main__":
    main()

# optimal solution using Boyer-Moore Voting Algorithm

def majority_element(nums):
    n = len(nums)
    result = []
    count1,count2 = 0,0
    el1,el2 = -1,-1
    for i in range(n):
        if count1 == 0 and nums[i] != el2:
            count1=1
            el1 = nums[i]
        elif count2 == 0 and nums[i] != el1:
            count2=1
            el2 = nums[i]
        elif el1 == nums[i]:
            count1 += 1
        elif el2 == nums[i]:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    
    count1, count2 = 0, 0
    for i in range(n):
        if nums[i] == el1:
            count1 += 1
        elif nums[i] == el2:
            count2 += 1
    if count1 > n // 3:
        result.append(el1)
    if count2 > n // 3:
        result.append(el2)
    return result
def main():
    nums = [1, 2, 3, 1, 1, 2, 1, 2, 2]
    print(majority_element(nums))
if __name__ == "__main__":
    main()