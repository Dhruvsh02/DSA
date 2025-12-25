# sort the linked list in ascending order 

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

# brute force approach : extract values, sort and recreate linked list
def sort_list_ll(head):
        if head is None or head.next is None:
            return head 
        arr = []
        temp = head 
        while temp:
            arr.append(temp.data)
            temp = temp.next 
        arr.sort()
        i = 0
        temp = head 
        while temp:
            temp.data = arr[i]
            i += 1
            temp = temp.next
        return head

# optimal approach : merge sort
def merge_sort_ll(head):
    if head is None or head.next is None:
        return head 
    slow = head 
    fast = head.next 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 

    mid = slow.next 
    slow.next = None 

    left = merge_sort_ll(head)
    right = merge_sort_ll(mid)
    return merge(left, right)

def merge(l1, l2):
    dummy = Node(0)
    curr = dummy 

    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next 

        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next 

    curr.next = l1 or l2
    return dummy.next

def main():
    arr = [4,2,1,3]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node

    print("Original Linked List:")
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

    head = merge_sort_ll(head)

    print("Sorted Linked List:")
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()