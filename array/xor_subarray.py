# XOR ing contigious subarray and 

from typing import List

def solve(A: List[int]) -> int:
    n = len(A)
    ans = 0 # will add values in it 
    for i in range(n):
        # Count how many subarrays include A[i]
        count = (i + 1) * (n - i)
        if count % 2 == 1:   # odd -> contributes
            ans ^= A[i]    # Xor using return 1 if dfferent and returns 0 if same value 
    return ans
    
def main():
    A = [1,3,5]
    result = solve(A)
    print(f"the subraay is using xor: {result}")
if __name__=="__main__":
    main()

