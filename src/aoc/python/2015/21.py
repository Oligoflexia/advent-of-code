from dataclasses import dataclass, field
from itertools import combinations
from python.utils.input_handler import get_input

input = get_input(2015, 21)

possible_items = {'Dagger': {'Cost': 8, 'Damage': 4, 'Armour': 0,},
           'Shortsword': {'Cost': 10, 'Damage': 5, 'Armour': 0,},
           'Warhammer': {'Cost': 25, 'Damage': 6, 'Armour': 0,},
           'Longsword': {'Cost': 40, 'Damage': 7, 'Armour': 0,},
           'Greataxe': {'Cost': 74, 'Damage': 8, 'Armour': 0,},
           'Leather': {'Cost': 13, 'Damage': 0, 'Armour': 1,},
           'Chainmail': {'Cost': 31, 'Damage': 0, 'Armour': 2,},
           'Splintmail': {'Cost': 53, 'Damage': 0, 'Armour': 3,},
           'Bandedmail': {'Cost': 75, 'Damage': 0, 'Armour': 4,},
           'Platemail': {'Cost': 102, 'Damage': 0, 'Armour': 5,},
           '': {'Cost': 0, 'Damage': 0, 'Armour': 0,},
           'Dmg+1': {'Cost': 25, 'Damage': 1, 'Armour': 0,},
           'Dmg+2': {'Cost': 50, 'Damage': 2, 'Armour': 0,},
           'Dmg+3': {'Cost': 100, 'Damage': 3, 'Armour': 0,},
           'Def+1': {'Cost': 20, 'Damage': 0, 'Armour': 1,},
           'Def+2': {'Cost': 40, 'Damage': 0, 'Armour': 2,},
           'Def+3': {'Cost': 80, 'Damage': 0, 'Armour': 3,}}

weapons = ['Dagger', 'Shortsword', 'Warhammer', 'Longsword', 'Greataxe',]
armours = ['Leather', 'Chainmail', 'Splintmail', 'Bandedmail', 'Platemail', '']
rings = ['Dmg+1', 'Dmg+2', 'Dmg+3', 'Def+1', 'Def+2', 'Def+3', '', '']

all_options = []

for weapon in weapons:
    for armour in armours:
        for ring1, ring2 in combinations(rings, 2):
            all_options.append([weapon, armour, ring1, ring2])

@dataclass
class Entity:
    name: str
    health: int = 100
    damage: int = 0
    armour: int = 0
    
    def defeated(self) -> bool:
        return self.health <= 0

    def take_dmg(self, dmg:int):
        if self.armour >= dmg:
            self.health -= 1
        else:
            self.health -= dmg - self.armour
    
    def attack(self) -> int:
        return self.damage

@dataclass
class Player(Entity):
    items: list = field(default_factory=list)
    cost: int = 0
    
    global possible_items
    
    def buy_items(self, purchases:list):
        for item in purchases:
            self.damage += possible_items[item]['Damage']
            self.armour += possible_items[item]['Armour']
            self.cost += possible_items[item]['Cost']
            self.items = purchases
  
def create_boss() -> Entity:
    global input  
    data = input.splitlines()

    hp = int(data[0].split(" ")[-1])
    dmg = int(data[1].split(" ")[-1])
    armr = int(data[2].split(" ")[-1])
    
    boss = Entity(name= 'Boss', health= hp, damage= dmg, armour= armr)
    return boss

def win(p: Player, b:Entity) -> bool:
    while not p.defeated():
        b.take_dmg(p.attack())
        if b.defeated():
            return True
        p.take_dmg(b.attack())
    return False

def cheapest_win():
    min_cost = float('inf')
    min_config = []
    
    global all_options
    
    for option in all_options:
        player = Player(name= 'Player')
        boss = create_boss()
        player.buy_items(option)
        
        if win(player, boss) and player.cost < min_cost:
            min_cost = player.cost
            min_config = option
    
    return min_cost, min_config

print(f"The cheapest cost of winning is: {cheapest_win()[0]} with the following items: {cheapest_win()[1]}")

def costliest_loss():
    max_cost = float('-inf')
    max_config = []
    
    global all_options

    for option in all_options:
        player = Player(name= 'Player')
        boss = create_boss()
        player.buy_items(option)
    
        if not win(player, boss) and player.cost > max_cost:
            max_cost = player.cost
            max_config = option
            
    return max_cost, max_config
    
print(f"The most expensive cost of losing is: {costliest_loss()[0]} with the following items: {costliest_loss()[1]}")