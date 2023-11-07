from dataclasses import dataclass, field
from queue import SimpleQueue
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

    def take_dmg(self, args:tuple):
        if args[1]:
            self.status.append(args[2])
        elif self.armour >= args[0]:
            self.health -= 1
        else:
            self.health -= args[0] - self.armour   
                    
    def attack(self) -> int:
        return self.damage, False, None
    
    def apply_ticks(self):
        for item in self.status:
            for condition, turns in item.items():
                if turns == 0:
                    self.status.remove(item)
                    if condition == 'Shield':
                        self.armour = 0
                    break
                match condition:
                    case 'Shield':
                        self.armour = 7
                    case 'Poison':
                        self.health -= 3
                    case 'Recharge':
                        self.mana += 110
                item[condition] -= 1

@dataclass
class Wizard(Entity):
    mana: int = 500
    health: int = 50
    spent_mana: int = 0
    
    def oom(self):
        return self.mana < 53
    
    def cast_missile(self):
        if not self.oom():
            self.mana -= 53
            self.spent_mana += 53
            return 4, False, None
        
    def cast_drain(self):
        if not self.oom():
            self.mana -= 73
            self.health += 2
            self.spent_mana += 73
            return 2, False, None
    
    def cast_shield(self):
        if not self.oom():
            self.mana -= 113
            self.spent_mana += 113
            self.status.append({'Shield': 6})
            return 0, False, None
            
    def cast_poison(self):
        if not self.oom():
            self.mana -= 173
            self.spent_mana += 173
            return 0, True, {'Poison': 6}
    
    def cast_recharge(self):
        if not self.oom():
            self.mana -= 229
            self.spent_mana += 229
            self.status.append({'Recharge': 5})
            return 0, False, None

player = Wizard(name= 'Player')
boss = Entity(name= 'Boss', health= 58, damage= 9)

while not player.defeated() and not player.oom():
    boss.apply_ticks()
    player.apply_ticks()
    if boss.defeated():
        print("You win!")
        break
    boss.take_dmg(player.cast_poison())
    if boss.defeated():
        print("You win!")
        break
    boss.apply_ticks()
    player.apply_ticks()
    if boss.defeated():
        print("You win!")
        break
    player.take_dmg(boss.attack())
    
def simulator(q:SimpleQueue, p:Wizard, b:Entity):
    while not q.empty():
        while not player.defeated() and not player.oom():
            player.apply_ticks()
            boss.apply_ticks()
            if boss.defeated():
                print("You win!")
                break
            boss.take_dmg(q.get())
            if boss.defeated():
                print("You win!")
                break
            boss.apply_ticks()
            player.apply_ticks()
            if boss.defeated():
                print("You win!")
                break
            player.take_dmg(boss.attack())


