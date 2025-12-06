# array to linked list 

arr = [10,20,30,40]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = Node(arr[0])
current = head 
for val in arr[1:]:
    current.next = Node(val)
    current = current.next 

# traversal of linked list

def traversal(head):
    temp = head
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("None")

traversal(head)

# length of linked list 

def length(head):
    temp = head 
    count = 0
    while temp:
        count +=1
        temp = temp.next
    return count

# search in linked list

def search(head,key):
    temp = head
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False

