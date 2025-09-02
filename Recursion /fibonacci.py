# fibonacci number 

def fib(n):
    if n<=1:
        return n
    # return fib(n-1)+fib(n-2)
    last=fib(n-1)
    slast=fib(n-2)
    return last+slast
def main():
    n=int(input("Enter the number: "))
    print(fib(n))
if __name__ == "__main__":
    main()
