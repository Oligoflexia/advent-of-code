from itertools import combinations
from utils.get_input import get_input

input = get_input(2015, 17)

containers = []
sol = []

for line in input.splitlines():
    containers.append(int(line))
    
for i in range(len(containers)):
    for combo in combinations(containers, i):
        if sum(combo) == 150:
           sol.append(combo)

print(f"The total number of combinations of filled containers that add up to 150L is {len(sol)}")

for i in range(len(containers)):
    num = len([x for x in sol if len(x) == i])
    if num == 0:
        pass
    else:
        print(f"The smallest number of containers that can add to 150L if filled is {i}")
        print(f"There are {num} such combinations where this is possible")
        break