# Problem 1 - Pokemon Class

class Pokemon:
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

    # Problem 2: Create Squirtle
    def print_pokemon(self):
      print({
          "name": self.name,   # Output: "name": "Squirtle",
          "types": self.types, # Output: "types": ["Water"],
          "is_caught": self.is_caught # Output: "is_caught": False
      })

    # Problem 4: Catch Pokemon
    def catch(self):
       self.is_caught = True

    # Problem 5: Choose Pokemon
    def choose(self):
        if self.is_caught == True:
            (f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")
    
    # Pokemon 6: Add Pokemon Type
    def add_type(self, type):
        self.types.append(type)
        
pikachu = Pokemon("Pikachu", ["Electric"]) 
squirtle = Pokemon("Squirtle", ["Water"])
charmander = Pokemon("Charmander", ["Fire"])

# Problem 3: Is Caught
squirtle.print_pokemon()
squirtle.is_caught = True
squirtle.print_pokemon()

my_pokemon = [pikachu, squirtle, charmander]

# Problem 7: Get Pokemon
def get_by_type(my_pokemon: list, pokemon_type:str ):
    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            pokemon.print_pokemon()

# get_by_type(my_pokemon, "Fire")

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

# Problem 8: Pokemon Evolution
def get_evolutionary_line(starter_pokemon: Pokemon):
  lst = []
  current_pokemon = starter_pokemon ## charmander
  while current_pokemon is not None:
    lst.append(current_pokemon.name)
    current_pokemon = current_pokemon.evolution
    print(lst)

charmander_list = get_evolutionary_line(charmander)

# Pokemon 9: Node Class
class Node:
   def __init__(self, value, next=None):
      self.value = value
      self.next = next

node_one = Node("a")

node_two = Node("b")

# Problem 10: Linking Nodes
node_one.next = node_two

print(node_one.value) 
print(node_one.next.value) 
print(node_two.value)
print(node_two.next) 


# node_1 = Node("Mario")
# node_2 = Node("Luigi")
# node_3 = Node("Wario")
# node_4 = Node("Toad")

# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4

# Problem 11: Mario Party
node_4 = Node("Toad")
node_3 = Node("Wario", node_4)
node_2 = Node("Luigi", node_3)
node_1 = Node("Mario", node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

# Problem 12: Printing Linked List
def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.value))
        head = head.next
    print("->".join(values))        

print_linked_list(node_1)