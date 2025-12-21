# add 1 to a number represented by linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# brute force approach

def reverse_ll(head):
    prev = None 
    front = None 
    temp = head 
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

def add_one_to_number_ll(head):
    head = reverse_ll(head)
    carry = 1
    temp = head 
    while temp and carry:
        temp.data += carry
        if temp.data == 10:
            temp.data = 0
            carry = 1
        else:
            carry = 0
        if temp.next is None and carry:
            temp.next = Node(1)
            break
        temp = temp.next
    return reverse_ll(head)

# optimal approach using recursion
def add_one_util(head):
    carry = helper(head)
    if carry == 1:
        new_node = Node(1)
        new_node.next = head
        head = new_node
    return head
def helper(temp):
    if temp is None:
        return 1
    carry = helper(temp.next)
    if carry == 0:
        return 0 
    temp.data += carry
    if temp.data < 10:
        return 0
    else:
        temp.data = 0
        return 1

def main():
    arr = [3, 5, 9]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = current.next
    
    new_head = add_one_to_number_ll(head)
    
    # Print the updated linked list
    temp = new_head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()

