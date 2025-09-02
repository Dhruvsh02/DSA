# check if two strings are anagram or not / valid anagram 
# brute force approach

def anagram(s,t):
    if len(s) != len(t):
        return False
    s_sorted = sorted(s)
    t_sorted = sorted(t)
    if s_sorted == t_sorted:
        return True
    return False

def main():
    s = 'eat'
    t = 'tea'
    result = anagram(s,t)
    print(f"valid anagram true or false: {result}")
if __name__ == "__main__":
    main()


# optimal approach

def anagram(s,t):
    if len(s) != len(t):
        return False
    freq_s = [0]*26
    freq_t = [0]*26
    for i in range(len(s)):
        freq_s[ord(s[i]) - ord('a')] += 1
        freq_t[ord(t[i]) - ord('a')] += 1
    if freq_s == freq_t:
        return True
    return False
def main():
    s = 'eat'
    t = 'tea'
    result = anagram(s,t)
    print(f"valid anagram true or false: {result}")
if __name__ == "__main__":
    main()