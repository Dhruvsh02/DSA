# inertion of a node in doubly linked list 

# insertion : at head (before)

class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

def insetion_head(head,data):
    new_head= Node(data)
    new_head.next = head
    new_head.prev = None
    head.prev = new_head
    return new_head

def main():
    arr = [20,45,67]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next 
    head = insetion_head(head,10)
    temp = head
    while temp:
        print(temp.data,end="<->")
        temp = temp.next
    print("None")   

if __name__ == "__main__":
    main()


# insertion : at tail (before)

def insertion_tail(head,data):
    new_node = Node(data)
    if head is None:
        return new_node
    tail = head 
    while tail.next:
        tail = tail.next
    prev = tail.prev 
    prev.next = new_node
    tail.prev = new_node
    new_node.prev = prev 
    new_node.next = tail
    return head
def main():
    arr = [20,45,67]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next 
    head = insertion_tail(head,10)
    temp = head
    while temp:
        print(temp.data,end="<->")
        temp = temp.next
    print("None")   

if __name__ == "__main__":
    main()


# insertion : kth position (before)


def insertion_at_position(head,position,data):
    new_node = Node(data)
    if head is None:
        if position==1:
            return new_node 
    if position == 1:
        new_node.next = head 
        head.prev = new_node
        return new_node
    temp = head
    count = 0 
    while temp:
        count+=1
        if count == position:
            break
        temp = temp.next
    
    prev = temp.prev
    prev.next = new_node
    temp.prev = new_node
    new_node.prev = prev
    new_node.next = temp
    return head
    
def main():
    arr = [20,45,67]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next 
    head = insertion_at_position(head,2,10)
    temp = head
    while temp:
        print(temp.data,end="<->")
        temp = temp.next
    print("None")
if __name__ == "__main__":
    main()

# insertion : value (before)

def insertion_by_value(node,data):
    new_node = Node(data)

    prev = node.prev 
    prev.next = new_node
    node.prev = new_node
    new_node.prev = prev
    new_node.next = node
    return new_node

def main():
    arr = [20,45,67]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next 

    insertion_by_value(head.next.next,10)
    temp = head
    while temp:
        print(temp.data,end="<->")
        temp = temp.next
    print("None")   
if __name__ == "__main__":
    main()