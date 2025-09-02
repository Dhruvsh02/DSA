# koko eating bananas : returns the minimum integer k such thatr koko can eat all bananas within h hours 
# linear apporach which will exceed time limit for large inputs
from math import ceil
def minEatingSpeed(piles, h):
     for i in range(1,max(piles)):
          required_hours = caneat(piles, i)
          if required_hours <= h:
                return i
          
     
def caneat(piles,h):
    hours = 0
    for i in range(len(piles)):
         hours += ceil(piles[i]/h)
    return hours 
    
def main():
    piles = [3,6,7,11] 
    h = 8
    print(minEatingSpeed(piles, h))
if __name__ == "__main__":
    main()

# now will use binary search to find the minimum k

def minEatingSpeed(piles, h):
    left , right = 1, max(piles)
    while left < right:
        mid = (left+right)//2
        total_hours = canEatAll(piles, mid)
        if total_hours <= h:
            right = mid-1
        else:
            left = mid + 1
    return left

def canEatAll(piles, speed):
    hours = 0
    for pile in piles:
         hours += ceil(pile/speed)
    return hours 
    
def main():
    piles = [3,6,7,11] 
    h = 8
    print(minEatingSpeed(piles, h))
if __name__ == "__main__":
    main()