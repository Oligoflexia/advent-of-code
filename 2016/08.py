from utils import helpers

input = helpers.get_input(2016, 8)

grid = [0 for _ in range(50*6)]

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

def rect(w:int, h:int, grd:list[int]) -> list[int]:
    for row in range(h):
        for col in range(w):
            grd[(row*50)+col] = 1
    
    return grd

def row_rotate(row:int, shift:int, grd:list[int]) -> list[int]:
    grd_cpy = grd[row*50:(row*50)+50].copy()
     
    for i, element in enumerate(grd_cpy):
        if element == 1:
            grd[row*50+i] = 0
            grd[row*50+((i+shift)%50)] = 1
    
    return grd


    

    
    

