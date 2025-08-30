# Problem Set Three

# Problem 1: Problem Circular List Length
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def circular_list_length(head: Node) -> int:
    '''Takes in a head node of a ll and returns the length of the cycle.'''
    length = 1

    current = head.next

    while current != head:
        current = current.next
        length += 1
    return length

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
num3.next = num1

num_ll_length = circular_list_length(num1)

print(num_ll_length)

# Problem #1.5: Cycle List Length
def cycle_list_length(head: Node) -> int:
    '''Takes in a head node of a ll and returns the length of a cycle.'''

    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            break
    else:
        return None
    
    cycle_length = 1

    slow_pointer = slow_pointer.next

    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        cycle_length += 1

    return cycle_length

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
num3.next = num2

print(cycle_list_length(num1))

# Problem 2: Detect and Remove Cycle in a Linked List
def detect_and_remove_cycle(head: Node) -> Node:
    '''Detects if a cycle is present and severs the connection. Returns head.'''
    if not head:
        return head

    slow_pointer = head
    fast_pointer = head

    # Step 1: Detect cycle
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            break
    else:
        return head  # no cycle

    # Step 2: Find start of cycle
    slow_pointer = head
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    # Step 3: Find node just before start of cycle
    cycle_start = slow_pointer
    ptr = cycle_start
    while ptr.next != cycle_start:
        ptr = ptr.next

    # Step 4: Break the cycle
    ptr.next = None

    return head

'''
Time: O(n) → Floyd’s detection + at most one full loop around the cycle.
Space: O(1) → only pointers used.
'''

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
num3.next = num2

updated_cycle = detect_and_remove_cycle(num1)

# Problem 3: Merge Two Sorted Linked Lists
def merge_two_lists(head_a: Node, head_b: Node) -> Node:
    '''Merge two sorted linked lists into one sorted linked list.'''
    dummy = Node(0)      # dummy head
    tail = dummy         # tail points to the end of the merged list

    while head_a and head_b:
        if head_a.value <= head_b.value:
            tail.next = head_a
            head_a = head_a.next
        else:
            tail.next = head_b
            head_b = head_b.next
        tail = tail.next   # move the tail forward

    # At least one list is finished; attach the remainder
    if head_a:
        tail.next = head_a
    if head_b:
        tail.next = head_b

    return dummy.next   # skip dummy and return real head

'''
Time: O(m + n), where m and n are lengths of the lists (we visit each node once).
Space: O(1), we only use a few pointers.
'''

ll_1 = Node(1, Node(2, Node(4)))
ll_2 = Node(2, Node(3, Node(4)))

ll_combo = merge_two_lists(ll_1, ll_2)

def print_ll(head: Node) -> print:
    while head:
        print(head.value, end= "->" if head.next else "\n")
        head = head.next

print_ll(ll_combo)

# Problem 4: Skip and Remove Nodes in a Linked List
def skip_and_remove(head: Node, m: int, n: int) -> Node:
    '''Keep m nodes, then delete n nodes, repeat until the end.'''
    if not head or m == 0:
        return None  # nothing to keep
    
    current = head
    
    while current:
        # --- Phase 1: Keep m nodes ---
        for _ in range(1, m):  # move m - 1 steps forward
            if not current:
                return head
            current = current.next

        if not current:  # reached end
            break

        # --- Phase 2: Delete next n nodes ---
        to_delete = current.next
        for _ in range(n):  # move n steps ahead to skip nodes
            if not to_delete:
                break
            to_delete = to_delete.next

        # reconnect the chain
        current.next = to_delete

        # move current pointer to the next kept node
        current = to_delete

    return head


'''
Time: O(n), since each node is visited once (kept or skipped).
Space: O(1), since only a few pointers are used.
'''

num10 = Node(10)
num9 = Node(9, num10)
num8 = Node(8, num9)
num7 = Node(7, num8)
num6 = Node(6, num7)
num5 = Node(5, num6)
num4 = Node(4, num5)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)

updated_ll = skip_and_remove(num1, 2, 3)
print_ll(updated_ll)

# Problem 5: Rotate a Doubly Linked List to the Left
class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

def rotate_left(head: Node, k: int) -> Node:
    '''Rotates a doubly linked list to the left by k places and returns new head.'''
    if not head or not head.next or k == 0:
        return head

    # Step 1: Find the length and the tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Normalize k
    k = k % length
    if k == 0:
        return head

    # Step 3: Find the new head after k steps
    new_head = head
    for _ in range(k):
        new_head = new_head.next
    
    new_tail = new_head.prev

    # Step 4: Re-link nodes
    new_tail.next = None
    new_head.prev = None
    tail.next = head
    head.prev = tail

    return new_head

'''
Time: O(n). Traversing once to get the length. Traversing again k steps to find new head. 
        Total ≤ 2 passes → linear.
Space: O(1). Only a few pointers (head, tail, new_head, new_tail) made.
'''

# Problem 6: Merge Nodes Between Zeros in a Linked List
def merge_nodes(head: Node) -> Node:
    '''Merges nodes between zeros into a single sum node and removes zeros.'''
    dummy = Node(0)  # dummy head for the new merged list
    merged_tail = dummy  # pointer to the last node of the merged list

    current = head.next  # skip the leading zero
    running_sum = 0

    while current:
        if current.value == 0:
            # when we hit a zero, commit the sum (if >0)
            if running_sum > 0:
                merged_tail.next = Node(running_sum)
                merged_tail = merged_tail.next
                running_sum = 0
        else:
            running_sum += current.value
        current = current.next

    return dummy.next

'''
Time Complexity: O(n). Each node is visited exactly once while summing.
Space Complexity: O(1). Only pointers and running_sum are used.
'''