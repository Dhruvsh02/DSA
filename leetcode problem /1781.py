# leetcode - 1781

def beautysum(s):
    n = len(s)
    total = 0
    for i in range(n):
        freq = [0]*26
        for j in range(i,n):
            char_ind = ord(s[j]) - ord('a')
            freq[char_ind] += 1

            max_freq = max(freq)
            min_freq = min([f for f in freq if f>0])

            total += (max_freq-min_freq)

    return total 

def main():
    s = 'aabcd'
    result = beautysum(s)
    print(f"the sum of beauty is : {result}")

if __name__=="__main__":
    main()