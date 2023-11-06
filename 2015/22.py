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

    def take_dmg(self, dmg:int, stat:bool, *args):
        if self.armour >= dmg:
            self.health -= 1
        else:
            self.health -= dmg - self.armour   
        if stat:
            self.status.append(arg)
                    
    def attack(self) -> int:
        return self.damage

@dataclass
class Wizard(Entity):
    mana: int = 500
    health: int = 50
    
    def oom(self):
        return mana < 53
    
    def cast_missile(self):
        if not oom():
            self.mana -= 53
            return 4
        
    def cast_drain(self):
        if not oom():
            self.mana -= 73
            self.health += 2
            return 2
    
    def cast_shield():
        pass
    
    def cast_poison():
        pass
    
    def cast_recharge():
        pass
    