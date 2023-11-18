from utils import helpers

input = helpers.get_input(2016, 8)

grid = [[0] * 50 for _ in range(6)]

steps = []

for line in input.splitlines():
    instructions = line.split(" ")   
    if instructions[0] == 'rotate': ins, val = [instructions[i] for i in [-3, -1]]
    else: ins, val = instructions
    steps.append([ins, val])
    
instructions = []

for step in steps:
    if step[0] == 'rect':
        a, b = step[1].split("x")
        instructions.append([step[0], a, b])
    else:
        a, b = step[0].split("=")
        instructions.append([a, b, step[1]])

# for i in instructions:
#     print(i)

