from utils.helpers import get_input

input = get_input(2015, 2)

def present_area(l, w, h):
    smallest = min(l*w, l*h, w*h)
    return 2*(l*w) + 2*(l*h) + 2*(w*h) + smallest

def calculate_sum(input):
    total = 0

    for line in input.splitlines():
        dimensions = line.split("x")
        
        total+=present_area(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))
    
    print(f"Total present area is: {total} square feet")


def calculate_ribbon(input):
    total = 0

    for line in input.splitlines():
        dimensions = line.split("x")
        
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        
        total+= (calculate_min_perimeter(l, w, h) + l*w*h)
    
    print(f"Total ribbon length is: {total} in.")
    return

def calculate_min_perimeter(a, b, c):
    return min(2*(a+b), 
               2*(a+c), 
               2*(b+c))

calculate_sum(input)
calculate_ribbon(input)
    

