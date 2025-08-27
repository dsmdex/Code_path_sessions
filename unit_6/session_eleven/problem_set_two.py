# Problem Set Two

# Problem 1: One to Many
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = Node("Mario", Node("Luigi", Node("Wario")))

tail = Node("Wario")
middle = Node("Luigi", tail)
head = Node("Mario", middle)

# Problem 2: Find Max
def find_max(head: Node) -> int:
    '''Finds and returns the maximum value in a given linked list.'''
    highest_value = None

    current = head

    while current:
        if not highest_value:
            highest_value = current.value
        else:
            if current.value > highest_value:
                highest_value = current.value
        current = current.next
    return highest_value

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(find_max(head))

'''
Time: Must traverse the entirety of the linked list, so worst case is O(n)
Space: Value tracker is initailized but is only updated on statement succession, O(1)
'''

# Problem 3: Remove Value
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
    # Check if the list is empty
    if head is None:
        return head

    # If the node to be removed is the head of the list
    if head.value == val:
        return head.next

    # Initialize pointers
    current = head.next
    previous = head

    # Traverse the list to find the node to remove
    while current:
        if current.value == val:
            previous.next = current.next
            return head
        previous = current
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head

# bug was that while loop had the incorrect check for stoppage, one positino too far ahead/
test_1 = Node(1, Node(2, Node(3, Node(4))))
test_1_result = remove_by_value(test_1, 4)
print(test_1_result.value)
print_list(test_1_result)


# Problem 4: Middle Match
def middle_match(head: Node, val: object) -> bool:
    '''Returns True if the val matches the middle Node, false otherwise.'''
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    if slow_pointer.value == val:
        return True
    return False

'''
Time: Must traverse the whole list in order to reach the end to find the mid point. So O(n)
Space: Simply updating pointer references, no new structures being made. O(1)'''

mid_test = Node(1, Node(2, Node(3, Node(4))))
print(middle_match(mid_test, 2))

# Problem 5: Where Do We Begin?
def get_loop_start(head: Node) -> bool:
    '''Returns True if a cycle is found in a linked list, false otherwise.'''
    
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            break
    else:
        return None
    
    slow_pointer = head
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    return slow_pointer.value

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_2


print(get_loop_start(node_1))

'''
Time: O(n) since you only ever traversing a set linked list, may be more than once to match but still O(n)
Space: O(1) no new data structures created.
'''

# Problem 6: Was that a Circuit?
def count_critical_points(head: Node) -> int:
    '''Returns the number of critical points in a linked list.'''
    
    prev = head
    current = head.next

    critical_count = 0

    while current:
        next_node = current.next
        if not next_node:
            break
        if prev.value < current.value and next_node.value < current.value:
            critical_count += 1
        elif prev.value > current.value and next_node.value > current.value:
            critical_count += 1
        prev = current
        current = next_node

    return critical_count

'''
Time: O(n) as we need to reach the end of the linked list to test the cases
Space: O(1) as nothing new is created in memory
'''

node = Node(1, Node(2, Node(3, Node(3, Node(3, Node(5, Node(1, Node(3))))))))
print(count_critical_points(node))