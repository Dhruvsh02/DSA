# representation of a node in a doubly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# array to doubly linked list   
def array_to_doubly_LL(arr):
    arr = [10,20,30,40]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = current.next
    return head 