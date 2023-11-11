from utils.helpers import get_input

input = get_input(2015, 15)

value_dict = {}

for line in input.splitlines():
    data = line.split(" ")
    
    value_dict[data[0][:-1]] = {
        data[1] : int(data[2][:-1]),
        data[3] : int(data[4][:-1]),
        data[5] : int(data[6][:-1]), 
        data[7] : int(data[8][:-1]),
        data[9] : int(data[10]),
    }
    
# for key in value_dict:
#     print(f"{key}: {value_dict[key]}")

# let f -> tsp of frosting
# let c -> tsp of candy
# let b -> tsp of butterscotch
# let s -> tsp of sugar

# t_capacity = f*4 + c*0 + b*-1 + s*0
# t_durability = f*-2 + c*5 + b*0 + s*0
# t_flavour = f*0 + c*-1 + b*5 + s*-2
# t_texture = f*0 + c*0 + b*0 + s*2
    
# optimization_fxn = t_cpacity * t_durability * t_flavour * t_texture
# optimization_fxn = (4*f - b) * (5*c - 2*f) * (5*b - 2*s - c) * (2*s)

# f + c + b + s = 100
# 0 <= f, c, b, s <= 100

# if t_capacity, t_durability, t_flavour, or t_texture < 0, then value == 0.

def generate_combinations(total_sum:int):
    combinations = []
    
    for a in range(total_sum + 1):
        for b in range(total_sum - a + 1):
            for c in range(total_sum - (a + b) + 1):
                d = total_sum - (a + b + c)
                combinations.append((a, b, c, d))
    
    return combinations

def calc_max_score(max_tsp:int) -> dict[int]:
    scores = {}
    
    for combo in generate_combinations(max_tsp):
        f = combo[0]
        c = combo[1]
        b = combo[2]
        s = combo[3]
        
        t_capacity = max(0, 4*f - b)
        t_durability = max(0, 5*c - 2*f)
        t_flavour = max(0, 5*b - 2*s - c)
        t_texture = max(0, 2*s)
        t_calories = max(0, 5*f + 8*c + 6*b + 1*s)
        
        score = t_capacity * t_durability * t_flavour * t_texture
        
        scores[score] = t_calories
    
    return(scores)

results = calc_max_score(100)
max_score = max(results.keys())

print(f"The maximum score possible is {max_score}")

calorie_match = max([v for v, c in results.items() if c == 500])

print(f"The maximum score possible for a cookie of 500 calories is {calorie_match}")

