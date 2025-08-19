# Node setup
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return str(self.val)


# Linked List setup
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return self.to_string()

    def to_string(self) -> str:
        """Return a string representation of the linked list."""
        values = []
        current = self.head
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)

    def print_linked_list(self):
        print(self.to_string())


# Problem 1: Reverse a singly linked list
def reverse_linked(head: Node) -> Node:
    """Reverse a linked list and return the new head."""
    current = head
    prev_node = None

    while current:
        next_node = current.next      # save next
        current.next = prev_node      # reverse pointer
        prev_node = current           # move prev forward
        current = next_node           # move current forward

    return prev_node


# Problem 2: Remove duplicates from sorted linked list
def remove_duplicates(head: Node) -> Node:
    """Remove duplicates from a sorted linked list and return the head."""
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next  # skip duplicate
        else:
            current = current.next            # move forward

    return head


# -------------------------
# Example runs
# -------------------------

# Reverse test
node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)
ll = LinkedList(node1)

print("Original list:")
ll.print_linked_list()

ll.head = reverse_linked(ll.head)
print("Reversed list:")
ll.print_linked_list()

# Remove duplicates test
node5 = Node(5)
node4 = Node(4, node5)
node3b = Node(3, node4)
node3a = Node(3, node3b)
node1 = Node(1, node3a)
ll2 = LinkedList(node1)

print("\nOriginal with duplicates:")
ll2.print_linked_list()

ll2.head = remove_duplicates(ll2.head)
print("After removing duplicates:")
ll2.print_linked_list()
