# Problem Set Three

# Problem 1: Calculate Torunament Place
class Player:
    def __init__(self, character: str, kart: str, outcomes: list):
        self.character = character
        self.kart = kart
        self.race_outcomes = outcomes
        self.average_placement = None
        self.items = []

    def get_tournament_place(self, opponents: list):
        # determine player average placement first
        placement_tally = 0
        avg_placement = 0

        for result in self.race_outcomes:
            placement_tally += result
        
        avg_placement = placement_tally / len(self.race_outcomes)
        self.average_placement = avg_placement

        opponent_list = len(opponents) + 1
        current_race_position = opponent_list

        for opponent in opponents:
            opp_placement_tally = 0
            opp_avg_placement = 0
            for result in opponent.race_outcomes:
                opp_placement_tally += result
                opp_avg_placement = opp_placement_tally / len(opponent.race_outcomes)
            
            if avg_placement < opp_avg_placement:
                current_race_position -= 1
            opp_placement_tally = 0
            opp_avg_placement = 0

        return current_race_position
    
player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(f"{player1.character} was number {player1.get_tournament_place(opponents)} with an average of {player1.average_placement}")


# Problem 2: Update Linked List Sequence
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # Problem 3
    def add_second(head: object, val: object) -> object:
        '''Takes in a head node and a val object, inserts the new val object as Node in the 2nd spot'''
        if not head:
            return None
        elif head.next:
            heads_next_node = head.next
            new_second_node = Node(val)
            head.next = new_second_node
            new_second_node.next = heads_next_node
        return head
    
    
red = Node('red')
yellow = Node('yellow')
blue = Node('blue')
red.next = yellow
yellow.next = blue

orange = Node("Orange")
green = Node("Green")

red.next = orange
orange.next = yellow
yellow.next = green
green.next = blue

# Problem 3: Insert Node as the Second Element
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)

new_num = 5

head = num1

def print_linked_list(head: Node) -> print:
    current = head

    while current:
        print(current.value)
        current = current.next

print()
print_linked_list(num1)

num1.add_second(new_num)

print()
print_linked_list(num1)

# Problem 4: Increment Linked List Node Values
def increment_ll(head: Node) -> Node:
    '''Takes in a head node of a linked list and increments each node value by 1.
        Returns the head once complete.'''
    current = head

    while current:
        current.value += 1
        current = current.next
    return head

num7 = Node(7)
num6 = Node(6, num7)
num5 = Node(5, num6)

my_list = num5

print()
# my_list: 5 -> 6 -> 7
print(my_list.value)

print()
print("origianl ll")
print_linked_list(my_list)

my_list = increment_ll(my_list)
# my_list: 6 -> 7 -> 8
print()
print("updated ll")
print_linked_list(my_list)

print()
my_list = increment_ll(my_list)
# my_list: 7 -> 8 -> 9
print("re-updated ll")
print_linked_list(my_list)


# Problem 5: Copy Linked List
def copy_ll(head: Node) -> Node:
    current = head

    copy_head = None
    next_node = None

    while current:
        if not copy_head:
            new_node = Node(current.value)
            copy_head = new_node
            next_node = copy_head
        else:
            new_node = Node(current.value)
            next_node.next = new_node
            next_node = new_node
        current = current.next

    return copy_head


num7 = Node(7)
num6 = Node(6, num7)
num5 = Node(5, num6)

head = num5

print()
# Linked List: 5 -> 6 -> 7
copy = copy_ll(head) # Linked List Copy: 5 -> 6 -> 7
print(head.value, copy.value)

# Change original list -- should not affect the copy
head.value = 10
print(head.value, copy.value)


# Problem 6: Find Minimum in Linked List
def find_min(head: Node) -> int:
    '''Takes in a head node of a linked list, returns the smallest value from it'''

    smallest_value = None

    current = head

    while current:
        if not smallest_value:
            smallest_value = current.value
        else:
            if smallest_value > current.value:
                smallest_value = current.value
        current = current.next

    return smallest_value

print(find_min(head))

# Problem 7: Remove Node by Value from Linked List
def ll_remove(head: Node, val: object) -> Node:
    '''Takes in a head node of a linked list and a value object, if a match is found, the node should be deleted.'''
    current = head
    prev_node = Node('dummy')
    prev_node.next = current

    while current:
        next_node = current.next
        if current.value == val and current == head:
            prev_node.next = next_node
            return next_node
        if current.value == val:
            prev_node.next = next_node
            return head
        prev_node = current
        current = next_node
    return None

num7 = Node(7)
num6 = Node(6, num7)
num5 = Node(5, num6)

head = num5

print()
print_linked_list(head)
print()
print(ll_remove(head, 6))
print()
print_linked_list(head)

# Problem 8: Remove Node by Value from Linked List
'''Version 1'''
def tail_to_head(head: Node) -> Node:
    """Move the tail of a linked list to the head (no prev_node needed)."""
    if not head or not head.next:
        return head  # empty or 1-node list, nothing to do
    
    current = head
    while current.next:
        if not current.next.next:  # current is second-to-last
            tail_node = current.next
            tail_node.next = head   # link tail to old head
            current.next = None     # chop tail off
            return tail_node
        current = current.next

'''Version 2'''
def tail_to_head_with_prev(head: Node) -> Node:
    """Move the tail of a linked list to the head (with prev_node tracking)."""
    if not head or not head.next:
        return head
    
    current = head
    prev_node = None

    while current:  # walk until tail
        if not current.next:  # found tail
            if prev_node:
                prev_node.next = None  # detach tail
            current.next = head        # attach tail to old head
            return current
        prev_node = current
        current = current.next

# Problem 9: Convert Singly Linked List to Doubly Linked List
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

crazy_in_love = Node("Crazy in Love")
formation = Node("Formation")
texas_hold_em = Node("Texas Hold 'Em")

crazy_in_love.next = formation
formation.next = texas_hold_em

formation.prev = crazy_in_love
texas_hold_em.prev = formation

# Problem 10: Find Length of Doubly Linked List from Any Node
def get_length(node: Node) -> len:
    '''Takes in a node at an unknown position, and returns the length of the doubly linked list it is in.'''

    current = node
    length_ahead = 0

    while current:
        length_ahead += 1
        current = current.next

    current = node
    length_behind = 0

    while current.prev:
        length_behind += 1
        current = current.prev

    total_length = length_ahead + length_behind

    return total_length


num7 = Node(7)
num6 = Node(6, num7)
num5 = Node(5, num6)

num7.prev = num6
num6.prev = num5

head = num6

print(get_length(head))