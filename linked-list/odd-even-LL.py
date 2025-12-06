class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
# brute force approach : O(n) space
def odd_even_ll(head):
    if head == None or head.next == None:
        return head
    arr = []
    temp = head
    while temp!= None and temp.next != None:
        arr.append(temp.data)
        temp = temp.next.next
    if temp:
        arr.append(temp.data)
    temp = head.next
    while temp!= None and temp.next != None:
        arr.append(temp.data)
        temp = temp.next.next
    if temp:
        arr.append(temp.data)
    i = 0
    temp = head
    while temp:
        temp.data = arr[i]
        i += 1
        temp = temp.next
    return head

# optimaized approach : O(1) space

def odd_even(head):
    if head == None or head.next == None:
        return head 
    odd = head
    even = head.next
    evenhead = head.next
    while even !=None and even.next != None:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next.next
    odd.next = evenhead
    return head


def main():
    arr = [1,2,3,4,5,6,7]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val) 
        current.next = new_node
        current = current.next
    head = odd_even_ll(head)   
    temp = head
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()