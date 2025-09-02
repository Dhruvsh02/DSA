'''
cut=1
def f():
    global cut 
    if cut==0:
        return 
    print(cut)
    cut=cut+1
    f()
def main():
    f()
if __name__ == "__main__":
    main()
'''

# print name n times using recusion 
'''
def print_name(n,i):
    if i>n:
        return 
    print("Aditi")
    print_name(n,i+1)
def main():
    n=5
    i=1
    print_name(n,i)
if __name__ == "__main__":
    main()
# print linerly from n to 1 using recursion 
'''
'''
def number(n,i):
    if i>n:
        return
    print(i)
    number(n,i+1)
def main():
    n= int(input("Enter the number: "))
    i=1
    number(n,i)
if __name__ == "__main__":
    main()
'''
'''
def number(n,i):
    if i<1:
        return
    print(i)
    number(n,i-1)
def main():
    n=int(input("Enter the number: "))
    i=1
    number(n,n)
if __name__ == "__main__":
    main()
'''
'''   
def number(n,i):
    if i<1:
        return
    number(n,i-1)
    print(i)
def main():
    n= int(input("Enter the number: "))
    i=1
    number(n,n)
if __name__ == "__main__":
    main()
'''
'''
def parameter(i,sum):
    if i<1:
        print(sum)
        return
    parameter(i-1,sum+i)
def main():
    i=int(input("Enter the number: "))
    sum=0
    parameter(i,sum)
if __name__ == "__main__":
    main()

'''
'''
def funcation(n):
    if n==0:
        return 0
    return n+funcation(n-1)
def main():
    n=int(input("Enter the number: "))
    print(funcation(n))
if __name__ == "__main__":
    main()
'''
'''
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
def main():
    n=int(input("enter number: "))
    print(fact(n))
if __name__ == "__main__":
    main()
'''