# delete all occurrences of a given key in doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def delete_occurrence_key_dll(head, key):
    if head is None:
        return None 
    
    temp = head 
    while temp:
        if temp.data == key:
            if temp == head:
                head = head.next 
            next_node = temp.next 
            prev_node = temp.prev
            if next_node:
                next_node.prev = prev_node
            if prev_node:
                prev_node.next = next_node
            temp = next_node
        else:
            temp = temp.next
    return head

def main():
    arr = [1,2,3,2,4,2,5]
    key = 2
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node

    print("Original Doubly Linked List:")
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

    head = delete_occurrence_key_dll(head, key)

    print(f"Doubly Linked List after deleting occurrences of {key}:")
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()
