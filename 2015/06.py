from utils.helpers import get_input
import numpy as np

input = get_input(2015, 6)

light_grid = np.zeros((1000, 1000), dtype=int)

# Takes an input line and provides a dict:
# - command (int)
# - 0 - turn off
# - 1 - turn on
# - 2 - toggle
#
# - start (tuple) - coords of start
# - end (tuple) - coords of end
def get_instructions(line):
    instructions = {}
    
    components = line.split(" ")
    
    if components[0] == 'toggle':
        instructions['command'] = 2
        instructions['start'] = tuple(map(int, components[1].split(',')))
        instructions['stop'] = tuple(map(int, components[3].split(',')))
    elif components[1] == 'on':
        instructions['command'] = 1
        instructions['start'] = tuple(map(int, components[2].split(',')))
        instructions['stop'] = tuple(map(int, components[4].split(',')))
    else:
        instructions['command'] = 0
        instructions['start'] = tuple(map(int, components[2].split(',')))
        instructions['stop'] = tuple(map(int, components[4].split(',')))
        
    return instructions
    
def make_changes(dict):
    x1, y1 = dict['start'][0], dict['start'][1]
    x2, y2 = dict['stop'][0], dict['stop'][1]

    if dict['command'] == 2:
        light_grid[x1:x2+1, y1:y2+1] ^= 1
    else:
        light_grid[x1:x2+1, y1:y2+1] = dict['command']
    return
        
def follow_directions(input):
    for line in input.splitlines():
        instructions = get_instructions(line)
        make_changes(instructions)
    print(f"There are {np.sum(light_grid)} lights on in total!")
    return

def change_brightness(dict):
    x1, y1 = dict['start'][0], dict['start'][1]
    x2, y2 = dict['stop'][0], dict['stop'][1]
    
    if dict['command'] == 0:
        light_grid[x1:x2+1, y1:y2+1] = np.maximum(light_grid[x1:x2+1, y1:y2+1]-1, 0)
    else:
        light_grid[x1:x2+1, y1:y2+1] += dict['command']
    return
        
def calculate_brightness(input):
    for line in input.splitlines():
        instructions = get_instructions(line)
        change_brightness(instructions)
    print(f"The total brightness is {np.sum(light_grid)}!")
    
        
follow_directions(input)

light_grid = np.zeros((1000, 1000), dtype=int)

calculate_brightness(input)


