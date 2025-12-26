# remove duplicates from a sorted doubly linked list
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None

def remove_duplicates_sorted_dll(head):
    temp = head 
    while temp and temp.next:
        nextnode = temp.next
        while nextnode and temp.data == nextnode.data:
            nextnode = nextnode.next
        temp.next = nextnode
        if nextnode:
            nextnode.prev = temp
        temp = temp.next
    return head

def main():
    arr = [1,1,1,2,3,3,4]
    head = Node(arr[0])
    current = head 
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node
    head = remove_duplicates_sorted_dll(head)
    print("Doubly linked list after removing duplicates:")
    temp = head
    while temp:
        print(temp.data, end="<->" if temp.next else "\n")
        temp = temp.next    
if __name__ == "__main__":
    main()