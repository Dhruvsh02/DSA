# deletion in linked list : head 

def delete_head(head):
    if head is None:
        return None
    temp = head
    head = head.next
    del temp 
    return head

def main():
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
    head = delete_head(head)
    temp = head
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("None")
if __name__ == "__main__":
    main()


# deletion in linked list : tail

def delete_tail(head):
    if head is None:
        return None
    if head.next is None:
        del head 
        return None 
    temp = head 
    while temp.next.next:
        temp = temp.next 
    to_delete = temp.next 
    temp.next = None 
    del to_delete
    return head

def main():
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
    head = delete_tail(head)
    temp = head 
    while temp:
        print(temp.data,end="->")
        temp = temp.next 
    print("None")

if __name__ == "__main__":
    main()


# deletion in linked list : at position

def delete_at_position(head,position):
    if head is None:
        return None 
    if position == 1:
        temp = head 
        head = head.next 
        del temp 
        return head 
    
    temp = head 
    prev = None
    count = 0 
    while temp is not None:
        count += 1
        if count == position:
            prev.next = prev.next.next
            del temp 
            break
        prev = temp
        temp = temp.next
    return head

def main():
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
    head = delete_at_position(head,3)
    temp = head 
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()

# deletion in linked list : by value

def delete_by_value(head,value):
    if head is None:
        return None
    if head.data == value:
        temp = head 
        head = head.next 
        del temp 
        return head 
    temp = head
    prev = None
    while temp:
        if temp.data == value:
            prev.next = prev.next.next
            del temp 
            break
        prev = temp 
        temp = temp.next 
    return head

def main():
    arr = [1,2,3,5,7]
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
    head = Node(arr[0])
    current = head 
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next

    head = delete_by_value(head,3)
    temp = head 
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("None")
if __name__ == "__main__":
    main()
