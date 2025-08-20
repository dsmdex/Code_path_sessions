# Problem Set One

# Problem 1: Battle Pokemon
class Pokemon:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, opponent):
        if opponent.hp - self.damage > 0:
            opponent.hp -= self.damage
            print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
        else:
            opponent.hp = 0
            print(f"{opponent.name} has fainted")
    
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)
pikachu.attack(opponent)
pikachu.attack(opponent)

# Problem 2: Convert to Linked List
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node_2 = Node("Wigglytuff")
node_1 = Node("Jigglypuff", node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)

# Problem 3: Add First
def add_first(head: Node, new_node: Node) -> Node:
    new_node.next = head
    return new_node

# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)

# Problem 4: Get Tail
def get_tail(head: Node) -> object:
    if not head:
        return None
    
    current = head
    tail = None
    
    while current:
        tail = current
        current = current.next
    
    return tail.value

num_3 = Node(3)
num_2 = Node(2, num_3)
num_1 = Node(1, num_2)

tail = get_tail(num_1)
print(tail)

# Problem 5: Replace Node
def ll_replace(head: Node, original: object, replacement: object) -> None:
    
    current = head

    while current:
        if current.value == original:
            current.value = replacement
        current = current.next

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5
head = num1

while head:
    print(head.value)
    head = head.next

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"

while head:
    print(head.value)
    head = head.next

# Problem 6: List Nodes
def listify_first_n(head: Node, n: int) -> list:
    list_of_n_nodes = []

    current = head
    count = 0

    while count < n:
        list_of_n_nodes.append(current.value)
        count += 1
        if current.next:
            current = current.next
        else:
            break


    return list_of_n_nodes

node_c = Node("c")
node_b = Node("b", node_c)
node_a = Node("a", node_b)

# linked list: a -> b -> c
head = node_a
lst = listify_first_n(head,2)
print(lst)

node_l = Node("l")
node_k = Node("k", node_l)
node_j = Node("j", node_k)
# linked list: j -> k -> l 
head2 = node_j
lst2 = listify_first_n(head2,5)
print(lst2)


# Problem 7: Insert Value
def ll_insert(head: Node, val: object, i: int) -> Node:
    # inserting at head
    if i == 0:
        new_node = Node(val)
        new_node.next = head
        return new_node
    
    current = head
    prev_node = None
    read_index = 0

    while current:
        if read_index == i:
            new_node = Node(val)
            prev_node.next = new_node
            new_node.next = current
            break
        prev_node = current
        current = current.next
        read_index += 1

    # if i is at the end, append
    if not current and read_index == i:
        new_node = Node(val)
        prev_node.next = new_node

    return head


node_9 = Node(9)
node_12 = Node(12, node_9)
node_8 = Node(8, node_12)
node_3 = Node(3, node_8)

head = node_3

new_head = ll_insert(head, 20, 0)
print(ll_insert(head, 20, 0))
print(listify_first_n(new_head, 5))

# Problem 8: Linked Listify
def list_to_linked_list(lst: list) -> Node:
    head = None
    current = head

    for item in lst:
        new_node = Node(item)
        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = current.next
    return head

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print(linked_list) # Only prints the head element!


# Problem 9: Doubly Linked List
class Node:
    def __init__(self, value: object, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

poliwrath = Node("Poliwrath")
poliwhirl = Node("Poliwhirl", poliwrath)
poliwag = Node("Poliwag", poliwhirl)

poliwrath.prev = poliwhirl
poliwhirl.prev = poliwag

print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)

# Problem 10: Print Backwards
def print_reverse(tail: Node) -> print:
    current = tail

    while current:
        print(current.value, end=" ")
        current = current.prev

print_reverse(poliwrath)
