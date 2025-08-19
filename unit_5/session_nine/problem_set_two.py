# Problem Set Two

# Problem 1: Card Class
class Card:
    def __init__(self, suit, rank, next = None):
        self.suit = suit
        self.rank = rank
        self.next = None

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    # Problem 2
    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    # Problem 4
    def is_valid(self):
        suits_of_cards = ["Hearts", "Spades", "Clubs", "Diamonds"]
        rank_of_cards = ['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        if self.suit in suits_of_cards and self.rank in rank_of_cards:
            return True
        return False
    
    # Problem 5
    def get_value(self):
        int_cards = [f"{x}" for x in range(2, 11)]
        
        if self.rank in int_cards:
            return int(self.rank)
        
        match self.rank:
            case "Ace":
                return 1
            case "Jack":
                return 11
            case "Queen":
                return 12
            case "King":
                return 13
            case _:
                return "Invalid"

            
card_eight = Card("Spades", "8")

# Problem 2: Print Card
card_suits = Card("Clubs", "Ace")
card_suits.print_card()

# Problem 3: Verify Update
card_suits.suit = "Hearts"
card_suits.print_card()

# Problem 4: Valid Card
my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())

# Problem 5: Get Value
card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())

# Problem 6: Hand Class
class Hand:
    def __init__(self):
        self.card = []

    def __repr__(self):
        return f"{self.card}"

    def add_card(self, card):
        self.card.append(card)
        
    def remove_card(self, card):
        self.card.remove(card)


card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []
print(player1_hand)

player1_hand.add_card(card_one)
# cards = [card_one]
print(player1_hand)

player1_hand.add_card(card_two)
# cards = [card_one, card_two]
print(player1_hand)

player1_hand.remove_card(card_one)
# cards = [card_two]
print(player1_hand)

# Problem 7: Sums of Cards
def sum_hand(hand: Hand) -> int:
    sum_of_cards = 0

    for card in hand.card:
        if card.is_valid():
            sum_of_cards += card.get_value()
        else:
            return None
    return sum_of_cards

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum)

# Problem 8: Print Hand
def print_hand(starting_card: Card) -> list:
    
    card_list = []
    current = starting_card

    while current:
        card_list.append(current)
        current = current.next
    return card_list

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

print(print_hand(card_one))

# Problem 9: Head and Tail Nodes
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}"

tail = Node(200)
head = Node(100, tail)

print()
print(head.value) 
print(head.next.value) 
print(tail.value) 
print(tail.next) 
# Problem 10: Middle Node
middle = Node(150, tail)
head.next = middle

print()
print(head.next.value) 
print(middle.next.value)
print(tail.next) 

# Problem 11: Zodiac Signs
node_4 = Node("Cancer")
node_3 = Node("Gemini", node_4)
node_2 = Node("Taurus", node_3)
node_1 = Node("Aries", node_2)

print()
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)


# Problem 12: Print Linked List
def print_linked_list(head: Node) -> list:
    
    node_list = []
    current = head

    while current:
        node_list.append(current)
        current = current.next
    
    return node_list

node_e = Node("e")
node_d = Node("d", node_e)
node_c = Node("c", node_d)
node_b = Node("b", node_c)
node_a = Node("a", node_b)

print(print_linked_list(node_a))