# find midddle of linked list

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

# brute force approach : calculate length of linked list
def middle_ll(head):
    if head is None:
        return None 
    temp = head 
    count = 0 
    while temp:
        count += 1
        temp = temp.next 
    mid = count // 2 + 1 
    temp = head 
    while temp and mid > 1:
        temp = temp.next
        mid -= 1
    return temp

# optimal appraoch : tortoise and hare algorithm - slow and fast pointer 
def optimal_middle_ll(head):
    if head is None:
        return None 
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def main():
    arr = [1,2,3,4,5,8,9,11,10,34]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    mid_node = optimal_middle_ll(head)
    if mid_node:
        print("Middle node data is:", mid_node.data)
    else:
        print("The linked list is empty.")

if __name__ == "__main__":
    main()