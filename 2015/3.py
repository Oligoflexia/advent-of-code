from utils.helpers import get_input

input = get_input(2015, 3)

test = ">>>>"

def travel(input):
    
    x = 0
    y = 0

    visited = []
    
    for move in input:
        coord = (x,y)
        
        if coord not in visited:
            visited.append(coord)
        
        if move == '>':
            x+=1
        elif move == '^':
            y+=1
        elif move == '<':
            x-=1
        else:
            y-=1
    
    print(f"The total # of unique houses visited by Santa (alone) is: {len(visited)}")
    return


def two_santas(input):
    real = {'x': 0, 'y':0}
    robo = {'x': 0, 'y':0}
    
    visited = [(0,0)]
    
    for index, move in enumerate(input):
        if index % 2 != 0:
            register_coord(robo, visited, move)
        else:
            register_coord(real, visited, move)
            
    print(f"The total unique # of houses visited by both Santas is: {len(visited)}")
    return
    
def register_coord(santa, list, move):
    if move == '>':
        santa['x']+=1
    elif move == '^':
        santa['y']+=1
    elif move == '<':
        santa['x']-=1
    else:
       santa['y']-=1
    
    coords = tuple(santa.values())
    if coords not in list:
        list.append(coords)
    
    return

travel(input)
two_santas(input)
       
