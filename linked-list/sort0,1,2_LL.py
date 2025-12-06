# sort linked list of 0s, 1s and 2s
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

# brute force approach : O(n) space
def sort_012_ll(head):
    if head == None or head.next == None:
        return head
    temp = head 
    count0 = 0
    count1 = 0
    count2 = 0
    while temp:
        if temp.data == 0:
            count0 += 1
        elif temp.data == 1:
            count1 += 1
        else:
            count2 += 1
        temp = temp.next
    temp = head
    while temp:
        if count0 > 0:
            temp.data = 0
            count0 -= 1
        elif count1 > 0:
            temp.data = 1
            count1 -= 1
        else:
            temp.data = 2
            count2 -= 1
        temp = temp.next
    return head

# optimal approach : O(1) space
def sort_012_ll_optimal(head):
    if head == None or head.next == None:
        return head
    zeroD = Node(-1)
    oneD = Node(-1)
    twoD = Node(-1)
    zero = zeroD
    one = oneD
    two = twoD
    temp = head
    while temp:
        if temp.data == 0:
            zero.next = temp
            zero = temp
        elif temp.data == 1:
            one.next = temp
            one = temp
        else:
            two.next = temp
            two = temp
        temp = temp.next
    zero.next = oneD.next if oneD.next != None else twoD.next
    one.next = twoD.next
    two.next = None
    head = zeroD.next
    return head



def main():
    arr = [1,2,0,1,2,0,1,0]
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = current.next
    head = sort_012_ll_optimal(head)
    temp = head
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()