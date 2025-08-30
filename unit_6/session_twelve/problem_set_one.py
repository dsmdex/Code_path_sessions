# Problem Set One

# Problem 1: Detect Circular Linked List
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head: Node) -> bool:
    '''Returns True if the linked list is circular, false otherwise.'''

    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer and slow_pointer == head:
            return True
    return False

'''
Time: O(n) Traversing until a circular linked list is found or the end is reached
Space: O(1) Only the pointers are intialized
'''

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)

num3.next = num1

print(is_circular(num1))

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)

print(is_circular(num1))

# Problem 2: Find Last Node in a Linked List Cycle
def find_last_node_in_cycle(head: Node) -> Node:
    """Returns the last node in a cycle if it exists, otherwise None."""
    
    # Phase 1: Detect if a cycle exists
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # No cycle found
        return None

    # Phase 2: Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    cycle_start = slow

    # Phase 3: Find the last node in the cycle
    current = cycle_start
    while current.next != cycle_start:
        current = current.next

    return current.value

'''
Time: O(n) → detection + traversal around the cycle.
Space: O(1) → only pointers.
'''

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)

num3.next = num1

print(find_last_node_in_cycle(num1))

# Print function
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Problem 3: Partition List Around Value
def partition(head: Node, val: object) -> Node:
    '''Rearranges the linked list so that all nodes < val come before nodes >= val. 
       Preserves original relative order within each partition.'''

    # dummy heads for before and after lists
    before_head = before_tail = Node(0)
    after_head = after_tail = Node(0)

    current = head

    while current:
        next_node = current.next
        current.next = None  # disconnect

        if current.value < val:
            before_tail.next = current
            before_tail = current
        else:
            after_tail.next = current
            after_tail = current

        current = next_node

    # stitch the two partitions
    before_tail.next = after_head.next
    return before_head.next

'''
Time Complexity (O(n)): Each node in the linked list is visited once during the traversal,
                            so the work grows linearly with the input size.
Space Complexity (O(1)): Only a constant number of extra pointers are used, 
                            and no additional data structures grow with the input size.
'''
    
node = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

result = partition(node, 3)

print_list(result)

# Problem 4: Convert Binary Number in a Linked List to Integer
def binary_to_int(head: Node) -> int:
    '''Takes in a h-node of a linked list and determines the decimal value of the binary input.'''
    binary_node = head

    final_binary_value = 0

    while binary_node:
        final_binary_value = final_binary_value * 2 + binary_node.value
        binary_node = binary_node.next

    return final_binary_value

'''
Time: Worst case scenario is O(n) as each node is visited once and stopped when the end is reached.
Space: O(1) since a few variables are initialized in memory and one updates a value.
'''


binary_ll = Node(1, Node(0, Node(1)))

decimal_value = binary_to_int(binary_ll)

print(decimal_value)


# Problem 5: Add Two Numbers Represented by Linked Lists
def add_two_numbers(head_a: Node, head_b: Node) -> int:
    '''Takes in two head nodes and that are non-negative and flips its representation, then summing
        the two together. Returns the sum.'''
    # Set the initial states
    dummy = Node(0)
    current = dummy
    carry = 0

    digit_a, digit_b = head_a, head_b

    # check for either ll to be true to keep adding values
    while digit_a or digit_b:
        a = digit_a.value if digit_a else 0
        b = digit_b.value if digit_b else 0

        # find sum of the two digits plus a carry over if applicable, or pass it one if necessary
        total = a + b + carry
        carry = total//10
        current.next = Node(total % 10)

        # shift over
        current = current.next

        # if the current digit is true, get the next one
        if digit_a:
            digit_a = digit_a.next
        if digit_b:
            digit_b = digit_b.next

        # if carry still exist by the end of both linked lists, include it as well
        if carry > 0:
            current.next = Node(carry)

        return dummy.next
    
'''
Time: O(n) as it must traverse to the end of both lists
Space: O(1) with a few variables being created initially
'''

# Problem 6: Reverse Sublist of a Linked List
def reverse_between(head, m, n):
    if not head or m == n:
        return head

    # Create a temporary head node to simplify edge cases where m is 1
    temp_head = Node(0)
    temp_head.next = head
    prev = temp_head

    # Step 1: Reach the node just before position m
    for i in range(m - 1):
        prev = prev.next
    
    # `prev` now is the node just before m, and `start` will be the first node to reverse
    start = prev.next
    then = start.next

    # Step 2: Reverse from m to n
    for _ in range(n - m):
        start.next = then.next  # Remove `then` from the list
        then.next = prev.next  # Insert `then` at the beginning of the reversed section
        prev.next = then  # Move `prev` to point to `then` as the new start of the reversed section
        then = start.next  # Move `then` to the next node to be reversed

    return temp_head.next

'''
Time Complexity: O(N) since we might need to traverse the entire list in the worst case.
Space Complexity: O(1) as we are using a constant amount of space regardless of the input size.
'''

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
new_head = reverse_between(head, 2, 5)
print_list(new_head)