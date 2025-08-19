# Problem Set Three

# Problem 1: Player Class
class Player:
    def __init__(self, character, kart, opponent = None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
    
    def __repr__(self):
        return f"{self.character + " - " + self.kart}"
    
    # Problem 2
    def get_player(self):
        return f"{self.character} is driving the {self.kart}"
    
    # Problem 4
    def set_player(self, name):
        possible_players = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
        if name in possible_players:
            self.character = name
            return "Character Updated"
        else:
            return "Invalid Character"
        
    # Problem 5
    def add_item(self, item_name: str) -> None:
        possible_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]

        if item_name in possible_items:
            self.items.append(item_name)

    # Problem 6
    def print_inventory(self):
        items_dict = {}

        if not self.items:
            print("Inventory: Empty")
            return

        for item in self.items:
            if item not in items_dict:
                items_dict[item] = 1
            else:
                items_dict[item] += 1
        print(items_dict)

player_one = Player("Yoshi", "Super Blooper")
print(player_one)

# Problem 2: Get Player
player_two = Player("Bowser", "Pirahna Prowler")
print(player_two.get_player())

def player_vs_player(player_one, player_two):
    print(f"Match: {player_one.get_player()} vs {player_two.get_player()}")

player_vs_player(player_one, player_two)

# Problem 3: Update Kart
player_one.kart = "Dolphin Dasher"
print(player_one.get_player())

# Problem 4: Set Character
print(player_one.set_player("Peach"))
print(player_two.set_player("Kermit"))

# Problem 5: Add Special Item
player_one = Player("Yoshi", "Dolphin Dasher")
# items = []
print(player_one.items)

player_one.add_item("red shell")
# items = ["red shell"]
print(player_one.items)

player_one.add_item("super star")
# items = ["red shell", "super star"]
print(player_one.items)

player_one.add_item("super smash")
# items = ["red shell", "super star"]
print(player_one.items)

# Problem 6: Print Inventory
player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()

# Problem 7: Race Results
def print_results(race_results):
    placement = 1
    for player in race_results:
        print(f"{placement}. {player.character}")
        placement += 1

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)

# Problem 8: Get Rank
def get_place(my_player):
    
    placement = 1

    current = my_player

    while current:
        if current.ahead:
            placement += 1
        current = current.ahead

    return placement

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
print(player1_rank)

player2_rank = get_place(peach)
print(player2_rank)

player3_rank = get_place(mario)
print(player3_rank)

# Problem 9: Tomy and Jerry
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


mouse = Node("Jerry")
cat = Node("Tom", mouse)

print(cat.value)
print(cat.next)
print(cat.next.value)
print(mouse.value)
print(mouse.next)

# Problem 10: Chase List
# dog = Node("Spike", cat)

# print(dog.value)
# print(dog.next)
# print(dog.next.value)
# print(cat.next)
# print(cat.next.value)
# try:
#     print(mouse.next.value)
# except:
#     print("None is next")


# Problem 11: Update Chase
cheese = Node("Gouda")
mouse.next = cheese

def print_linked_list(head: Node):
    current = head

    while current:
        print(current.value, end="->")
        current = current.next

print_linked_list(cat)

# Problem 12: Chase String
def chase_list(head: Node) -> str:
    final_string = ''
    current = head

    while current:
        final_string += current.value
        if current.next:  # only add "chases" if not last
            final_string += " chases "
        current = current.next
    
    return final_string


dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print()
print(chase_list(dog))