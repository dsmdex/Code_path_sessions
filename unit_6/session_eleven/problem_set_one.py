# Problem Set One

# Problem 1: Nested Constructors
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node = Node(4, Node(3, Node(2)))

head = node

while head:
    print(head.value)
    head = head.next

'''
Time: O(n)
Space: O(1)
'''

# Problem 2:
def count_elements(head: Node, val: object) -> int:
    count = 0

    while head:
        if head.value == val:
            count += 1
        head = head.next

    return count

print(count_elements(node, 2))

'''
Time: Worst case scenario involves traversing the entire linked list. So O(n)
Space: Initialization of the count variable is created once and only incremented afterwards. So O(1)'''

# Problem 3: Remove Tail, find and correct the bug!
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


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

print_list(node)
remove_tail(node)
print_list(node)

'''
Time: Must traverse the entire linked list to reach the tail, so O(n)
Space: No new data structures created, O(1)
'''

# Problem 4: Find the Middle
def find_middle_element(head: Node) -> Node:
    '''Find the middle element of a linked list, returns the second middle node if even.'''
    
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer  = fast_pointer.next.next

    return slow_pointer.value

test = Node(1,Node(2,Node(3,Node(4))))
print_list(test)
print(find_middle_element(test))

'''
Time: Must reach the end of the list to determine the middle point. O(n)
Space: No new data strucures created, so O(1)'''


# Problem 5: Is Palindrome?
def is_palindrome(head: Node) -> bool:
    '''Takes in a linked list and determines whether it is a palidrome or not.'''
    # traverse the list to find the midway point, then stop
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    # relink the second half of the linked list to reverse it
    prev = None
    current = slow_pointer

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    # check both values to see if a palindrome exists
    first_half = head
    reversed_second_half = prev

    while reversed_second_half:
        if reversed_second_half.value != first_half.value:
            return False
        first_half = first_half.next
        reversed_second_half = reversed_second_half.next
    return True

node = Node(1, Node(2, Node(3)))
print(is_palindrome(node))
node = Node(1, Node(2, Node(1)))
print(is_palindrome(node))

'''
Time: O(n+n+n) which is 3n but gets reduced to n, so is O(n)
Space: Initial creation for pointers, but nothing more is made, so O(1)
'''

# Problem 6: Put it in Reverse
def reverse(head: Node) -> Node:
    '''Takes in a linked list, reverse it in place. and returns the new head(which was the tail)'''

    current = head
    prev = None
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

node = Node(4, Node(3, Node(2, Node(1))))

print_list(node)
reversed_node = reverse(node)
print(reversed_node)
print_list(reversed_node)