# remove the nth node from the end of a linked list

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
# brute force approach : two traversals
def remove_nth_fromend(head,n):
    count = 0
    temp = head 
    while temp:
        count+=1
        temp = temp.next
    if n == count:
        return head.next
    temp = head
    res = count - n
    for _ in range(res - 1):
        temp = temp.next
    temp.next = temp.next.next
    return head

# optimal approach : using one traversal 
def remove_nth_fromend_optimal(head,n):
    fast = head
    for _ in range(n):
        fast = fast.next
    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next
    if fast == None:
        return head.next
    delete_node = slow.next
    slow.next = slow.next.next
    return head

def main():
    arr = [1,2,3,4,5]
    n = 2
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = current.next
    head = remove_nth_fromend(head,n)
    temp = head
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()