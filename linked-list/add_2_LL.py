# add 2 numbers in a linked list 

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
def adding_ll(head1,head2):
    t1 = head1
    t2 = head2
    dummynode = Node(-1)
    carry = 0
    current = dummynode
    while t1 or t2:
        sum = carry
        if t1 :
            sum = sum + t1.data
        if t2 :
            sum = sum + t2.data
        new_node = Node(sum%10)
        carry = sum//10
        current.next = new_node
        current = current.next
        if t1:
            t1 = t1.next
        if t2:
            t2 = t2.next
        if carry:
            new_node = Node(carry)
            current.next = new_node

    return dummynode.next

def main():
    arr1 = [2,4,6]
    arr2 = [5,8,9]
    head1 = Node(arr1[0])
    head2 = Node(arr2[0])
    head1 = Node(arr1[0])
    curr = head1
    for i in arr1[1:]:
        curr.next = Node(i)
        curr = curr.next

    head2 = Node(arr2[0])
    curr = head2
    for i in arr2[1:]:
        curr.next = Node(i)
        curr = curr.next
    result = adding_ll(head1,head2)

    while result:
        print(result.data, end=" -> ")
        result = result.next
    print("None")


if __name__ == "__main__":
    main()