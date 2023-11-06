from dataclasses import dataclass, field
from utils.get_input import get_input

input = get_input(2015, 22)

@dataclass
class Entity:
    name: str
    health: int = 100
    damage: int = 0
    armour: int = 0
    status: list = field(default_factory = list)
    
    def defeated(self) -> bool:
        return self.health <= 0

    def take_dmg(self, dmg:int, stat:bool = False, *args):
        if stat:
            self.status.append(args)
        if self.armour >= dmg:
            self.health -= 1
        else:
            self.health -= dmg - self.armour   
                    
    def attack(self) -> int:
        return self.damage
    
    def apply_ticks(self):
        for item in self.status:
            for condition, turns in item:
                if turns == 0:
                    self.status.remove(item)
                match condition:
                    case 
                

@dataclass
class Wizard(Entity):
    mana: int = 500
    health: int = 50
    
    def oom(self, n:int):
        return self.mana < int
    
    def cast_missile(self):
        if not self.oom(53):
            self.mana -= 53
            return 4
        
    def cast_drain(self):
        if not self.oom(73):
            self.mana -= 73
            self.health += 2
            return 2
    
    def cast_shield(self):
        if not self.oom(113):
            self.mana -= 113
            self.status.append(('Shield', 6))
            return 0
            
    def cast_poison(self):
        if not self.oom(173):
            self.mana -= 173
            return 0, True, ('Poison', 6)
    
    def cast_recharge(self):
        if not self.oom(229):
            self.mana -= 229
            self.status.append(('Recharge', 5))
            return 0