from utils.get_input import get_input
from itertools import permutations

input = get_input(2015, 13)

guests = set()
values = {}

for line in input.splitlines():
    data = [line.split(" ")[i] for i in [0, 2, 3, 10]]
    data[2] = int(data[2])
    data[3] = data[3][:-1]
    guests.add(data[3])
    
    if data[1] == 'gain':
        data[1] = 1
    else:
        data[1] = -1
    
    if data[0] not in values:
        values[data[0]] = {}

    values[data[0]][data[3]] = data[1] * data[2]

def calc_happiness(s:set) -> int:
    val = [None]*len(s)
    
    s = list(s)
    
    val[0] = values[s[0]][s[1]] + values[s[0]][s[-1]]
    val[-1] = values[s[-1]][s[0]] + values[s[-1]][s[-2]]
    
    for i in range(1, len(val) -1):
        val[i] = values[s[i]][s[i-1]] + values[s[i]][s[i+1]]
    
    return sum(val)

max = float('-inf')

for perm in permutations(guests, len(guests)):
    v = float(calc_happiness(perm))
    if v > max:
        max = v
        optimal = list(perm)

print(f"The maximum happiness value for these guests is: {int(max)}")

for key in values:
    values[key]['Soup'] = 0

values['Soup'] = {}

for guest in guests:
    values['Soup'][guest] = 0
    
guests.add('Soup')

max = float('-inf')

for perm in permutations(guests, len(guests)):
    v = float(calc_happiness(perm))
    if v > max:
        max = v
        optimal = list(perm)

print(f"The maximum happiness value once I'm added is: {int(max)}")