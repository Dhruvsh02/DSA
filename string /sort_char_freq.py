from collections import Counter
# sort characters by frequency
# for lowercase letters only
def frequencysort(s):
    freq = [(0,chr(i+ord('a'))) for i in range(26)]

    for ch in s:
        index = ord(ch) - ord('a')
        freq[index] = (freq[index][0] + 1,ch )
    freq.sort(key = lambda x: (-x[0] , x[1]))
    result = [ch for f,ch in freq if f > 0]
    return result 

def main():
    s = "tree"
    result = frequencysort(s)
    print(f"sort characters by frequency: {result}")
if __name__=="__main__":
    main()


# for all characters 
def freq_sort(s):
    freq = Counter(s)
    sorted_chars = sorted(freq.items() , key = lambda x: (-x[1],x[0]))
    result = ''.join([ch*count for ch,count in sorted_chars])
    return result
def main():
    s = "tree"
    result = freq_sort(s)
    print(f"sort characters by frequency: {result}")
if __name__=="__main__":
    main()
