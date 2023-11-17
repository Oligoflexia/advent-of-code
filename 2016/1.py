from utils.helpers import get_input

input = get_input(2016, 1)

directions = input.split(", ")

orientations = {0: "North", 1:"East", 2:"South", 3:"West"}

position = {'x':0, 'y':0, 'direction': 0}

def direction_finder(pos:dict, directions) -> (int, int):
    global orientations
    
    for step in directions:
        if step[0] == 'L':
            pos['direction'] -= 1
        else:
            pos['direction'] += 1
    
        match orientations[pos['direction'] % 4]:
            case "North":
                pos['y'] += int(step[1:])
            case "East":
                pos['x'] += int(step[1:])
            case "South":
                pos['y'] -= int(step[1:])
            case "West":
                pos['x'] -= int(step[1:])
    return pos['x'], pos['y']

print(direction_finder(position, directions))

position = {'x':0, 'y':0, 'direction': 0}

def duplicate_direction_finder(pos:dict, directions) -> (int, int):
    global orientations
    
    visited = [(0,0)]
    
    for step in directions:
        if step[0] == 'L':
            pos['direction'] -= 1
        else:
            pos['direction'] += 1
    
        match orientations[pos['direction'] % 4]:
            case "North":
                for i in range(pos['y'] + 1, pos['y'] + int(step[1:])):
                    if (pos['x'], i) in visited:
                        return pos['x'], i
                    else: visited.append((pos['x'], i))
                pos['y'] += int(step[1:])
                
                    
            case "East":
                for i in range(pos['x'] + 1, pos['x'] + int(step[1:])):
                    if (i, pos['y']) in visited:
                        return i, pos['y']
                    else: visited.append((i, pos['y']))
                pos['x'] += int(step[1:])
            
                
            case "South":
                for i in range(pos['y'] - 1, pos['y'] - int(step[1:]), -1):
                    if (pos['x'], i) in visited:
                        return pos['x'], i
                    else: visited.append((pos['x'], i))
                pos['y'] -= int(step[1:])
                
                    
            case "West":
                for i in range(pos['x'] - 1, pos['x'] - int(step[1:]), -1):
                    if (i, pos['y']) in visited:
                        return i, pos['y']
                    else: visited.append((i, pos['y']))
                pos['x'] -= int(step[1:])

        
        if (pos['x'], pos['y']) in visited:
            return pos['x'], pos['y']
        else: visited.append((pos['x'], pos['y']))

print(duplicate_direction_finder(position, directions))