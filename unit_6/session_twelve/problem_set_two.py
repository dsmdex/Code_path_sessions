# Problem Set Two

# Problem 1: Convert a Singly Linked List to a Circular Linked List
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def make_circular(head: Node) -> Node:
    '''Takes in a singly linked list and converts it into a circular linked list. Returns the head.'''

    if not head:
        return None

    current = head
    tail_node = None

    while current:
        tail_node = current
        current = current.next
    tail_node.next = head
    return head

'''
Time: O(n) dependent on the input size and will traverse the entire linked list.
Space: O(1) only initial variables are created in memory.
'''

circular_test = Node(1, Node(2, Node(3)))
circular_check = make_circular(circular_test)
n = 0

while n < 4:
    print(circular_check.value)
    circular_check = circular_check.next
    n += 1

# Problem 2: Collect Nodes of a Cycle in a Linked List
def collect_cycle_node(head: Node) -> list:
    # detect cycle
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            break
    else:
        return []

    # find cycle start
    slow_pointer = head
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    cyclic_start = slow_pointer

    # collect cycle nodes
    cyclic_elements = []
    current = cyclic_start
    while True:
        cyclic_elements.append(current.value)
        current = current.next
        if current == cyclic_start:
            break

    return cyclic_elements


'''
Time: O(n) — detection, finding cycle start, and traversal are each linear in the size of the list.
Space: O(k) where k is the length of the cycle (since you store cycle nodes in a list). 
        It’s not technically O(n) in all cases, but worst-case k == n.
'''

# Problem 3: Delete Duplicati in a Linked List
def delete_dupes(head: Node):
    '''Takes in a head node of a linked list and returns the same ll with duplicates removed as well
        as their first instances.'''
    current = head

    prev = Node(0)
    prev.next = current

    # in the event the event the head has a duplicate, keep our prev reference in case we need to
    #   access prev.next for the new head
    copy_of_prev = prev

    while current:
        next_node = current.next
        if next_node and current.value == next_node.value:
                dupli_value = current.value
                while current and current.value == dupli_value:
                    next_node = current.next
                    current = next_node
                prev.next = next_node
        prev = current
        current = next_node
    return copy_of_prev.next

'''
Time: Time Complexity: O(n), since each node is visited at most once as duplicates 
        are skipped in a single forward traversal without restarting from the head.
Space: Only pointer variables are made so O(1)'''

dupe_ll = Node(1, Node(1, Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))))

def print_ll(head: Node) -> print:
    '''Prints out the linked list. Returns None'''

    while head:
        print(head.value, end= "->" if head.next else "\n")
        head = head.next

print_ll(dupe_ll)
deleted_nodes = delete_dupes(dupe_ll)
print_ll(deleted_nodes)

# Problem 4: Identical Linked Lists
def is_identical(head_a: Node, head_b: Node) -> bool:
    '''Takes in two linked lists with their respective head nodes and returns True if they're the same,
        False otherwise.'''

    while head_a and head_b:
        if head_a.value != head_b.value:
            return False
        head_a = head_a.next
        head_b = head_b.next

    return head_a is None and head_b is None

'''
Time: Must traverse both lists to the end, only visits each node once. O(n)
Space: Only pointers are created in memory, O(1)
'''

ll_1 = Node(1, Node(1, Node(3, Node(4))))
ll_2 = Node(1, Node(2, Node(3, Node(4))))

print(is_identical(ll_1, ll_2))

# Problem 5: Circular Linked List Route
# def rotate_right(head: Node, k: int) -> Node:
#     '''Takes in a linked list head, and k parameter. Shifts the linked list to the right, k times.
#         Returns the head.'''
    
#     if k == 0 or not head.next or not head:
#         return head
    
#     # n represents the total cycles done
#     n = 0

#     current = head
#     dummy = Node(0)
#     dummy.next = head
#     prev = dummy


#     while n < k:
#         if current.next:
#             prev = current
#             current = current.next
#         else:
#             current.next = head
#             prev.next = None
#             head = current
#             n+= 1

#     return head

# '''
# Time: O(k) since out k input determines how many cycles we need to perform.
# Space: O(1) since we only create the pointers.
# '''

'''Version works but is very inefficient if k is a large size. Rather than making repetitive rotations,
    we should only worry about the final rotations, not any cycles that will be made.
'''

def rotate_right(head: Node, k: int) -> Node:
    '''Rotates the linked list to the right by k places and returns the new head.'''
    if not head.next or k == 0 or not head:
        return head
    
    # first determine the length and reach the end of the linked list
    length_of_ll = 1
    tail = head

    while tail.next:
        tail = tail.next
        length_of_ll += 1

    # determine how the shifts we wil need
    k = k % length_of_ll

    if k == 0:
        return head
    
    # connect the tail to the head
    tail.next = head

    # find the new tail for the updated link list
    # how many steps to reach the new tail?
    length_to_new_tail = length_of_ll - k
    
    # initialize a new reference for the new tail
    new_tail = head

    # find the new head by traversing the linked list again
    for _ in range(length_to_new_tail - 1):
        new_tail = new_tail.next
    
    # severe the connection of the circle. leaving new_tail as the tail
    #   and new head sa the new head
    new_head = new_tail.next
    new_tail.next = None

    return new_head

'''
Time: O(n). One traversal to find length. One traversal to find new_tail. Becomes ~2n → O(n).
Space: O(1) Only a few pointers
'''

node_ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))

rotation_test = rotate_right(node_ll, 6)
print_ll(rotation_test)
        

# Problem 6: Circular Linked List Delete
def delete_node(head: Node, val: int) -> Node:
    '''Deletes the first instance of val from a circular linked list. Returns the (possibly new) head.'''
    if not head:
        return None
    
    current = head
    prev = None

    while True:
        if current.value == val:
            if prev:  # deleting a non-head node
                prev.next = current.next
                return head
            else:  # deleting the head
                # if it's the only node
                if current.next == head:
                    return None
                # otherwise, find the tail to fix the circular link
                tail = head
                while tail.next != head:
                    tail = tail.next
                head = current.next
                tail.next = head
                return head

        prev = current
        current = current.next
        if current == head:  # full cycle, value not found
            break
    
    return head

'''
Time: O(n). In the worst case, we may traverse the entire list once to either find 
        the node or confirm it's not there.
Space: O(1), few pointers created in memory.
'''
d_3 = Node(3)
d_2 = Node(2, d_3)
d_1 = Node(1, d_2)
d_3.next = d_1

deletion_test = delete_node(d_1, 1)
print(deletion_test.next.next.next.value)