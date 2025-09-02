'''
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    # Precompute frequency
    hash_arr = [0] * 13  # Assuming numbers are in range 0–12
    for num in arr:
        hash_arr[num] += 1

    q = int(input())
    for _ in range(q):
        number = int(input())
        print(hash_arr[number])

# Run
main()
'''
'''
def main():
    # Read string input
    s = input()

    # Initialize hash array for 26 lowercase letters
    hash_arr = [0] * 26

    # Count frequency of each character
    for ch in s:
        hash_arr[ord(ch) - ord('a')] += 1 # ord(ch) gives the ASCII value of the character
        # ord('a') gives the ASCII value of 'a' which is 97

    # Process queries
    q = int(input())
    for _ in range(q):
        ch = input().split()[0]  # Read the character # splits into a list of words # [0] gets the first word
        print(hash_arr[ord(ch) - ord('a')])

main()



'''

#map hashing 
from collections import defaultdict

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    # Precompute frequency using defaultdict
    # defaultdict(int) initializes the default value to 0 for non-existing keys
    # used in python and in c++ used is map<int,int> freq;

    freq = defaultdict(int)

    for num in arr:
        # used in python to increment the value of the key
        # freq[num] += 1; used in c++
        freq[num] += 1
        # for itrate in the map 
    
    
    # for key , value in freq.items():
    #      print(f"{key}->  {value}")
    
    
    q = int(input())
    for _ in range(q):
        number = int(input())
        print(freq[number])

main()
