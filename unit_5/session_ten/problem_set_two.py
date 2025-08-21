# Problem Set Two

# Problem 1: Two-Pair Hand
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

def is_two_pair(player_hand: list) -> bool:
    '''Takes in a player hand list that consists of 5 Card objects. 
       Returns True if a two-pair exists, False otherwise.'''

    pairs = 0
    counted_ranks = set()   # <-- track ranks we already used for a pair

    card_one_index = 0
    card_two_index = 0
    hand_length = len(player_hand)

    card_one = player_hand[card_one_index]
    card_two = player_hand[card_two_index]

    while pairs < 2 and card_one_index < hand_length:
        if card_one_index != card_two_index and card_one.rank == card_two.rank:
            if card_one.rank not in counted_ranks:   # <-- only count rank once
                pairs += 1
                counted_ranks.add(card_one.rank)

            # move to next card_one after finding a pair
            card_one_index += 1
            if card_one_index < hand_length:
                card_one = player_hand[card_one_index]
            card_two_index = 0
            card_two = player_hand[card_two_index]
        else:
            card_two_index += 1
            if card_two_index < hand_length:
                card_two = player_hand[card_two_index]
            else:
                # finished scanning this card_one, move to next
                card_one_index += 1
                if card_one_index < hand_length:
                    card_one = player_hand[card_one_index]
                card_two_index = 0
                if card_one_index < hand_length:
                    card_two = player_hand[card_two_index]

    return pairs >= 2


card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))

'''
Time Complexity: O(1) -> Avoids O(n**2) only due to the fact that the hand is a fixed number.
Space Complexity: O(1) -> At most adds in 2 pairs, so constant
'''

# Problem 2: Update Linked List Sequence
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node_4 = Node("Ken")
node_3 = Node("Weird Barbie", node_4)
node_2 = Node("President Barbie", node_3)
node_1 = Node("Barbie", node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

# Problem 3: Insert Value First
def add_first(head: Node, val: object) -> Node:
    new_node = Node(val)
    new_node.next = head
    head = new_node
    return head

add_first(node_1, 0)

# Problem 4: Linked List Length
def ll_length(head: Node) -> int:
    '''Takes in a head Node of a linked list and returns the length of that linked list'''

    current = head
    total_length = 0

    while current:
        total_length += 1
        current = current.next

    return total_length

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)

# Linked List: num1 -> num2 -> num3
head = num1
print(ll_length(head))

# Empty Linked List
head = None
print(ll_length(head))

# Problem 5: Delete Tail
def delete_tail(head: Node) -> None:
    '''Takes in a head Node of a Linked List and removes the tail, returns None'''

    current = head

    while current.next:
        if not current.next.next:
            current.next = None
        else:
            current = current.next 

delete_tail(node_1)

# Problem 6: Greatest Node
def find_max(head: Node) -> object:
    '''Takes in a head node of a linked list, returns the node with the maximum value'''

    current = head
    highest_node = None
    highest_node_value = None

    while current:
        if not highest_node_value:
            highest_node = current
            highest_node_value = current.value
        elif current.value > highest_node_value:
            highest_node = current
            highest_node_value = current.value
        current = current.next

    return highest_node.value


num4 = Node(10)
num3 = Node(30, num4)
num2 = Node(15, num3)
num1 = Node(20, num2)

# linked list: num1 -> num2 -> num3 -> num4
max_val = find_max(num1)
print(max_val)


# Problem 7: Pop Node
def ll_pop(head: Node, i: int) -> Node:
    '''Removes the node at index i, returns the new head'''

    if i == 0:
        return head.next  # pop the head directly
    
    current = head
    read_index = 0
    
    # stop one before the node to delete
    while current and current.next:
        if read_index == i - 1:
            current.next = current.next.next
            return head
        current = current.next
        read_index += 1
    
    return head  # if i is out of bounds, return unchanged head


num4 = Node(10)
num3 = Node(30, num4)
num2 = Node(15, num3)
num1 = Node(20, num2)

ll_pop(num1, 1)

current = num1

print()
while current:
    print(current.value)
    current = current.next

# Problem 8: Find Middle Node
def find_middle_node(head: Node) -> Node:
    '''Takes in a head node and finds the middle node of a linked list and returns it'''
    
    slow_node = head
    fast_node = head

    while fast_node and fast_node.next:
        slow_node = slow_node.next
        fast_node = fast_node.next.next

    return slow_node.value

num5 = Node(11)
num4 = Node(10, num5)
num3 = Node(30, num4)
num2 = Node(15, num3)
num1 = Node(20, num2)

print()
print(find_middle_node(num1))

# Problem 9: Create Double Links
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

head = Node("First")
tail = Node("Last")

head.next = tail
tail.prev = head

print(head.value, "<->", head.next.value)
print(tail.prev.value, "<->", tail.value)

# Problem 10: Double to Single
class SLLNode:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class DLLNode:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
def dll_to_sll(dll_head):
    current = dll_head
    sll_head = None
    tail = None   # keep track of the end of the SLL

    while current:
        new_node = SLLNode(current.value)

        if not sll_head:
            # first node becomes the head
            sll_head = new_node
            tail = new_node
        else:
            # connect the last node to the new node
            tail.next = new_node
            tail = new_node  # advance the tail

        current = current.next
    
    return sll_head.value  # return the head of the new SLL

node_steam = Node("Steam")
node_water = Node("Water", node_steam)
node_ice = Node("Ice", node_water)

node_steam.prev = node_water
node_water.prev = node_ice

print(dll_to_sll(node_ice))