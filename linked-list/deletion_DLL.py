# deletion of a node in doubly linked list : head
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


def delete_head(head):
    if head is None:
        return None
    if head.next is None:
        del head 
        return None
    prev = head 
    head = head.next
    head.prev = None
    prev.next = None
    del prev
    return head

def main():
    arr = [20,12,13,24,56]
    head = Node(arr[0])
    current = head 
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next 
    head = delete_head(head)
    temp = head 
    while temp:
        print(temp.data,end="<->")
        temp = temp.next
    print("None")
if __name__ == "__main__":
    main()

# deletion of a node in doubly linked list : tail

def delete_tail(head):
    if head is None:
        return None
    if head.next is None:
        del head 
        return None
    tail = head
    while tail.next is not None:
        tail = tail.next
    prev = tail.prev
    tail.prev = None
    prev.next = None
    del tail 

    return head

def main():
    arr = [98,7,5,6]
    head = Node(arr[0])
    current = head 
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next 
    head = delete_tail(head)
    temp = head 
    while temp:
        print(temp.data,end="<->")
        temp = temp.next
    print("None")   

if __name__ == "__main__":
    main()


# deletion of a node in doubly linked list : at position 

def delete_at_position(head,position):
    temp = head 
    count = 0
    while temp:
        count +=1
        if count == position:
            break
        temp = temp.next
    prev = temp.prev
    front = temp.next
    if prev == None and front == None:
        del temp 
        return None
    elif prev == None:
        delete_head(head)
        return head
    elif front == None:
        delete_tail(head)
        return head
    else:
        prev.next = front
        front.prev = prev 
        temp.next = None
        temp.prev = None
        del temp
        return head
def main():
    arr = [2,5,6,7,8,9]
    head = Node(arr[0])
    current = head 
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next 

    head = delete_at_position(head,3)
    temp = head
    while temp:
        print(temp.data,end="<->")
        temp = temp.next
    print("None")   
if __name__ == "__main__":  
    main()


# deletion in linked list : value 

def delete_node(temp):
    if temp is None or temp.prev is None:
        return None
    
    prev = temp.prev
    front = temp.next

    if front == None:
        prev.next = None
        temp.prev = None
        del temp 
        return None

    prev.next = front
    front.prev = prev 
    temp.prev = None
    temp.next = None 
    del temp
    return None


def main():
    arr = [12,5,6,8]
    head = Node(arr[0])
    current = head 
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next

    delete_node(head.next)
    temp = head 
    while temp:
        print(temp.data,end="<->")
        temp = temp.next
    print("None")
if __name__ == "__main__":
    main()


