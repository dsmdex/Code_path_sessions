# Problem Set Three

# Problem 1: The Power of One
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

ll = Node("Ash", Node("Misty", Node("Brock")))

# Problme 2: Frequency Map
def frequency_map(head: Node) -> dict:
    '''Takes in the head of a linked list and returns a dictionary mapping 
    each unique element to the number of times it appears.'''
    element_count = {}

    while head:
        if head.value not in element_count:
            element_count[head.value] = 1
        else:
            element_count[head.value] += 1
        head = head.next
    return element_count

'''
Time: O(n). Worst case scenario involves traversing the entire linked list in order to update the frequency.
Space: O(n). Worst case, if all elements are unique, the dictionary will store n entries.'''

map_test = Node(1, Node(2, Node(3, Node(4, Node(2, Node(3))))))
print(frequency_map(map_test))

# Problem 3: Get it Out of Here!
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Function with a bug!
def remove_by_value(head, val):
    # Handle empty list and removal from the head
    if not head:
        return None
    if head.value == val:
        return head.next  # Return the second node as the new head

    current = head
    while current.next:
        if current.next.value == val:
            current.next = current.next.next  # Skip the node with the value
            return head  # Return the original head
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head

removal_test = Node(1, Node(2, Node(3, Node(4))))
remove_me = remove_by_value(removal_test, 3)
print_list(remove_me)

# Problem 4: Does it Cycle?
def has_cycle(head: Node) -> bool:
    '''Detects whether a linked list contains a cycle using the 
    two-pointer (Floyd’s tortoise and hare) technique.'''
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True
    return False

'''
Time: O(n). In the worst case, the fast pointer will traverse at most O(n)
                steps before either reaching the end (no cycle) or meeting the slow pointer (cycle exists).
Space: O(1) as only pointer variables are created for tracking.'''

cy4 = Node(4)
cy3 = Node(3, cy4)
cy2 = Node(2, cy3)
cy1 = Node(1, cy2)
cy4.next = cy1

print(has_cycle(cy1))

# Problem 5: Are We There Yet?
def cycle_length(head: Node) -> int:
    '''If the linked list contains a cycle, return its length (number of nodes in the cycle). Otherwise return None'''
    # first, check and see if it is a cycle to beign with
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            break
    else:
        return None
    
    # if a cycle, find the distance from the head to the cycle start node
    # move fast pointer up by one so while loop can execute
    cycle_len = 1
    fast_pointer = fast_pointer.next

    while slow_pointer != fast_pointer:
        fast_pointer = fast_pointer.next
        cycle_len += 1

    return cycle_len

'''
Time: O(n) as the linked list must be traversed until the end is reached or a cycle is found
Space: O(1) as only the pointers and counter are made in memory. 
'''

cy4 = Node(4)
cy3 = Node(3, cy4)
cy2 = Node(2, cy3)
cy1 = Node(1, cy2)
cy4.next = cy2
    
print(cycle_length(cy1))

# Problem 6: Reverse Them, K?
def reverse_first(head: Node, k: int) -> Node:
    '''Takes in a linked list head node and reverse all k elements, returns new head of the ll.'''
    
    new_tail = head

    prev = None
    current = head
    traversal_count = 0

    while traversal_count < k and current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        traversal_count += 1
    
    new_tail.next = current

    return prev

'''
Time: O(k) — reverses at most k nodes. If k exceeds list length n, it reverses the entire list.
Space: O(1) — only a few pointers are used.
'''

cy5 = Node(5)
cy4 = Node(4, cy5)
cy3 = Node(3, cy4)
cy2 = Node(2, cy3)
cy1 = Node(1, cy2)
reverse_test = (reverse_first(cy1, 20))
print(reverse_test.value)
print_list(reverse_test)