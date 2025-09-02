# maximum consecutive ones in an array

def maxconsecutive_ones(arr):
    max_count = 0 
    count =  0 
    for i in range(len(arr)):
        if arr[i] == 1:
            count +=1
            max_count = max(count, max_count)
        else: 
            count = 0 
    return max_count
def main():
    arr = [1,1,0,1,1,1]
    result = maxconsecutive_ones(arr)
    print("The maximum consecutive ones are: ", result)
if __name__ == "__main__":
    main() 