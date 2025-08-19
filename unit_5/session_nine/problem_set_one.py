# Problem Set One
# Problem 1: Pokemon Class
class Pokemon:
    def __init__(self, name: str, types: list, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        # Problem 8
        self.evolution = evolution
    
    def __repr__(self):
        return self.name
    
    # Problem 2
    def print_pokemon(self):
        print({
            "name": self.name,
            "typing": self.types,
            "has been caught": self.is_caught
        })

    # Problem 4
    def catch(self):
        self.is_caught = True

    # Problem 5
    def choose(self):
        if self.is_caught:
            print(f"{self.name}, I choose you")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

    # Problem 6
    def add_type(self, new_type):
        self.types.append(new_type)

pikachu = Pokemon("Pikachu", ["Electric"])

# Problem 2: Create Squirtle
squirtle = Pokemon("Squirtle", ["Water"])
squirtle.print_pokemon()

# Problem 3: Is Caught
squirtle.is_caught = True
squirtle.print_pokemon()

# Problem 4: Catch Pokemon
rattata = Pokemon("Rattata", ["Normal"])
rattata.print_pokemon()
rattata.catch()
rattata.print_pokemon()

# Problem 5: Choose Pokemon
pikachu.choose()
pikachu.catch()
pikachu.choose()

# Problem 6: Add Pokemon Typing
jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()

# Problem 7: Get Pokemon
def get_by_type(my_pokemon: list, pokemon_type: str) -> list:
    '''Takes in a list of Pokemon objects and a typing to check for, returns matching list'''
    matching_pokemon = []

    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            matching_pokemon.append(pokemon)
    
    return matching_pokemon

diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)

# Problem 8: Pokemon Evolution
def get_evolutionary_line(starter_pokemon: Pokemon) -> list:
    evolution_line = [starter_pokemon]
    
    while starter_pokemon.evolution:
        evolution_line.append(starter_pokemon.evolution)
        starter_pokemon = starter_pokemon.evolution

    return evolution_line

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)

# Problem 9: Node Class
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

node_two = Node("b")
node_one = Node("a")

print(node_one.value) 
print(node_one.next) 
print(node_two.value)
print(node_two.next) 

# Problem 10: Linking 
node_one.next = node_two
print(node_one.value)
print(node_one.next.value)
print(node_two.value)

# Problem 11: Mario Party
toad = Node("Toad")
wario = Node("Wario", toad)
luigi = Node("Luigi", wario)
mario = Node("Mario", luigi)

print(mario.value, "->", mario.next.value)
print(luigi.value, "->", luigi.next.value)
print(wario.value, "->", wario.next.value)
print(toad.value, "->", toad.next)

# Problem 12 Printing Linked List
def print_linked_list(head: Node) -> str:
    
    current = head

    while current:
        print(current.value, end="->")
        current = current.next

print_linked_list(mario)