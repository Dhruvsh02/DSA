# insertion in the linked list : head 
class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
def insert_at_head(head,data):
    new_node = Node(data)
    new_node.next = head 
    return new_node

def main():
    arr = [30,20,40,4]
    head = Node(arr[0])
    current = head 
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next 
    head = insert_at_head(head,10)
    temp = head
    while temp:
        print(temp.data,end="->")
        temp = temp.next

    print("None")
if __name__ == "__main__":
    main()


# insertion in the linked list : tail

def insert_at_tail(head,data):
    if head is None:
        return Node(data)
    new_node = Node(data)
    temp = head 
    while temp.next != None:
        temp = temp.next
    temp.next = new_node
    return head

def main():
    arr = [1,2,3,4]
    head = Node(arr[0])
    current = head 
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    head = insert_at_tail(head,5)
    temp = head 
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("None")
if __name__ == "__main__":
    main()

# insertion in the linked list : position  

def insert_at_position(head,position,data):
    if head is None:
        if position == 1:
            return Node(data)
        else:
            return None
    if position == 1:
        new_node = Node(data)
        new_node.next = head 
        return new_node 
    
    temp = head 
    count = 0 
    while temp is not None:
        count +=1
        if count == position - 1:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
            break
        temp = temp.next
    return head

def main():
    arr = [1,4,5,7]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    head = insert_at_position(head,3,10)
    temp = head 
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("None")

if __name__ == "__main__":  
    main()

# insertion in the linked list : after a given node 

def insert_after_node(head,prev_node,data):
    if head is None or prev_node is None:
        return head 
    if head.data == prev_node:
        new_node = Node(data)
        new_node.next = head.next
        head.next = new_node
        return head
    temp = head
    while temp:
        if temp.data == prev_node:
            new_node = Node(data)
            new_node.next = temp.next 
            temp.next = new_node
            break
        temp = temp.next
    return head

def main():
    arr = [4,7,8,9]
    head = Node(arr[0])
    current = head 
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next 
    head = insert_after_node(head,8,10)
    temp = head 
    while temp:
        print(temp.data,end="->")
        temp = temp.next 
    print("None")   

if __name__ == "__main__":
    main()