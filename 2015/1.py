from utils.get_input import get_input

input = get_input(2015, 1)

def final_floor(string):
    floor = 0
    
    for letter in string:
        if letter == '(':
            floor+=1
        else:
            floor-=1
    print(f"The final floor is: {floor}")
    return

def when_basement(input):
    floor = 0
    i = 0
    
    for letter in input:
        if letter == '(':
            floor+=1
        else:
            floor-=1
        
        i+=1
        
        if floor < 0:
            print(f"Index when entering basement is {i}")
            return
        
    print("never in basement")
    
final_floor(input)
when_basement(input)