# number of substring containing all three characters  

# brute force approach using loops and set time complexity O(n^2)

def countSubstring(s: str) -> int:
    n = len(s)
    count = 0
    for i in range(n):
        hash_set = [0] * 3
        for j in range(i,n):
            hash_set[ord(s[j]) - ord('a')] = 1
            if hash_set[0] + hash_set[1] + hash_set[2] == 3:
                # count = count + 1
                count = count + (n-j)
                break
    return count

# test cases
print(countSubstring("bbacba"))


# optiaml approach using sliding window 

def optimal_countSubstring(s: str) -> int:
    n = len(s)
    lastseen = [-1] * 3
    count = 0
    for i in range(n):
        lastseen[ord(s[i]) - ord('a')] = i
        if lastseen[0] != -1 and lastseen[1] != -1 and lastseen[2] != -1:
            count = count + (min(lastseen) + 1)
    return count

# test cases
print(optimal_countSubstring("bbacba"))