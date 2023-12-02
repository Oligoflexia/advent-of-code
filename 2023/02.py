from utils.input_formatter import SplitStringInput
import re
from math import prod

InputObject, input_str_list = SplitStringInput.return_input(2, 2023)

game_bounds = {"red": 12, "green": 13, "blue": 14}
round_max = {}

i = 1

valid_ids = []

for all_rounds in input_str_list:
    valid = True
    first_split = all_rounds.split(": ")
    
    round_data = re.findall(r"\d+\s(?:red|blue|green)", first_split[1])
    
    while valid:
        for element in round_data:
            data = element.split(" ")
            value = int(data[0])
            colour = data[1]
            
            if game_bounds[colour] < value:
                valid = False
                break
        if valid: 
            valid_ids.append(i)
        valid = False
    i += 1
            
print(sum(valid_ids))

for all_rounds in input_str_list:
    round_max[i] = {}
    valid = True
    first_split = all_rounds.split(": ")
    
    round_data = re.findall(r"\d+\s(?:red|blue|green)", first_split[1])
    
    for element in round_data:
        data = element.split(" ")
        value = int(data[0])
        colour = data[1]
        
        if colour not in round_max[i]:
            round_max[i][colour] = value
        if value > round_max[i][colour]:
            round_max[i][colour] = value
    i += 1
            
t_num = 0

for nums in round_max.values():
    t_num += prod(nums.values())

print(t_num)