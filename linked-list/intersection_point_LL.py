# find the internsection point of Y linked lists

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

# brute force approach

def intersection_point_ll(head1, head2):
    nodes_set = set()
    temp = head1
    while temp:
        nodes_set.add(temp)
        temp = temp.next
    temp = head2
    while temp:
        if temp in nodes_set:
            return temp
        temp = temp.next
    return None

# optimal approach
def optimal_intersection_point_ll(head1, head2):
    t1 = head1
    t2 = head2
    n1 = 0
    n2 = 0
    while t1:
        n1 += 1
        t1 = t1.next
    while t2:
        n2 += 1
        t2 = t2.next
    d = abs(n1 - n2)
    if n1 > n2:
        for _ in range(d):
            head1 = head1.next
    else:
        for _ in range(d):
            head2 = head2.next
    while head1 and head2:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return None

# new optimal approach using two pointers

def optimal_new_intersection_point_ll(head1, head2):
    if head1 is None or head2 is None:
        return None 
    temp1 = head1
    temp2 = head2 
    while temp1 != temp2:
        temp1 = temp1.next
        temp2 = temp2.next
        if temp1 == temp2:
            return temp1
        if temp1 is None:
            temp1 = head2
        if temp2 is None:
            temp2 = head1
    return temp1


def main():
    # Common part (intersection)
    common = Node(6)
    common.next = Node(2)

    # First linked list: 3 → 1 → 4 → 6 → 2
    head1 = Node(3)
    head1.next = Node(1)
    head1.next.next = Node(4)
    head1.next.next.next = common

    # Second linked list: 1 → 2 → 4 → 5 → 6 → 2
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(4)
    head2.next.next.next = Node(5)
    head2.next.next.next.next = common

    result = optimal_new_intersection_point_ll(head1, head2)

    if result:
        print("Intersection at node with data:", result.data)
    else:
        print("No intersection")

if __name__ == "__main__":
    main()