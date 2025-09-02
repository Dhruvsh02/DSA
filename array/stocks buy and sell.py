# best time to buy and sell stock to get maximum profit

def max_profit(arr,cost):
    n = len(arr)
    max_profit = 0
    min_price = arr[0]
    for i in range(1,n):
        cost = arr[i] - min_price
        max_profit = max(max_profit,cost)
        min_price = min(min_price,arr[i])
    return max_profit
def main():
    arr = [7,1,5,3,6,4]
    cost = 0
    result = max_profit(arr,cost)
    print("The maximum profit is: ", result)
if __name__ == "__main__":
    main()
