from python.utils import input_handler

input = input_handler.get_input(2016, 8)

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

def rect(w:int, h:int, grd:list[int], grid_l:int = 50) -> list[int]:
    for row in range(h):
        for col in range(w):
            grd[(row*grid_l)+col] = 1

def row_rotate(row:int, shift:int, grd:list[int], grid_l:int = 50) -> list[int]:
    grd_cpy = grd[row*grid_l:(row*grid_l)+grid_l].copy()
     
    for i in range(len(grd_cpy)):
            grd[row*grid_l+(i+shift)%grid_l] = grd_cpy[i]

def col_rotate(col:int, shift:int, grd:list[int], grid_l:int = 50, grid_h:int = 6) -> list[int]:
    grd_cpy = grd.copy()
    
    for i in range(col, len(grd), grid_l):
        grd[(i+(shift*grid_l))%(grid_l*grid_h)] = grd_cpy[i]

def solve(grd, ins_list) -> int:
    for inst in ins_list:
        match inst[0]:
            case 'y':
                row_rotate(int(inst[1]), int(inst[2]), grd)
            case 'x':
                col_rotate(int(inst[1]), int(inst[2]), grd)
            case 'rect':
                rect(int(inst[1]), int(inst[2]), grd)

    return sum(grd)

print(f"There are {solve(grid, instructions)} lit pixels after swiping the card \n")

decoded_grid = ["#" if _ == 1 else "." for _ in grid]
print("The final code on the screen is:")
print("".join(decoded_grid[:50]))
print("".join(decoded_grid[50:100]))
print("".join(decoded_grid[100:150]))
print("".join(decoded_grid[150:200]))
print("".join(decoded_grid[200:250]))
print("".join(decoded_grid[250:300]))


    

