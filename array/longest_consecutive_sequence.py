# brute force approach

def longest_consecutive_sequence(arr):
    n = len(arr)
    longest = 1
    for i in range(n):
        count = 1
        x = arr[i]
        while x + 1 in arr:
            count += 1
            x += 1
        longest = max(longest, count)
    return longest

def main():
    arr = [100, 4, 200, 1, 3, 2]
    result = longest_consecutive_sequence(arr)
    print("The length of the longest consecutive sequence is: ", result)
if __name__ == "__main__":
    main()


# better approach 

def longest_consecutive_sequence(arr):
    n = len(arr)
    arr.sort()
    longest = 1
    count_curr = 1 
    last_smaller = -1
    for i in range(n):
        if arr[i] - 1 == last_smaller:
            count_curr += 1 
            last_smaller = arr[i]
        elif arr[i] != last_smaller:
            count_curr = 1
            last_smaller = arr[i]
        longest = max(longest, count_curr)
    return longest
def main():
    arr = [1,1,1,2,2,3,4,4,4,5,100,102,101,102,104,105,103,106,108,107]
    result = longest_consecutive_sequence(arr)
    print("The length of the longest consecutive sequence is: ", result)
if __name__ == "__main__":
    main()

# optimal approach

def longest_consecutive_sequence(arr):
    n = len(arr)
    num_set = set(arr)
    longest = 1
    for i in range(n):
        num_set.add(arr[i])
    for num in arr:
        if num - 1 not in num_set:
            count = 1
            x = num
            while num + count in num_set:
                count += 1
                x = x + 1
            longest = max(longest, count)
    return longest

# we can use nium_set = {} this is optimize my code and give accurate result
# also then we will use num_set.keys(): this will check for the keys in the set and also we will replace num_set.add with num_set[num]
# will give a accurate result with time complexity of O(n) and space complexity of O(n)
# num_set = {}
#     count = 0

#     for num in nums:
#        num_set[num] = 1
    
#     for num in num_set.keys():
#       if num-1 in num_set.keys(): continue
#       longest = 1
#       while num+1 in num_set.keys():
#         num += 1
#         longest += 1 



def main():
    arr = [100, 4, 200, 1, 3, 2]
    result = longest_consecutive_sequence(arr)
    print("The length of the longest consecutive sequence is: ", result)
if __name__ == "__main__":  
    main()
 