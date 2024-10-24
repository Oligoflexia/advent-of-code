from python.utils.input_handler import get_input
from itertools import combinations
import math

input = get_input(2015, 24)

weights = [int(number) for number in input.splitlines()]
total_weight = sum(weights)
compartment_weight = total_weight // 3

print(f"The total weight of all packages is {total_weight}, which means each compartment weighs {compartment_weight}.")

def find_smallest_group_brute(num_list:list[int]) -> (int, list[int]):
    compartment_weight
    for i in range(3, len(num_list)):
        combos = combinations(num_list, i)
        
        for combo in combos:
            if sum(combo) == compartment_weight:
                return i, combo

#print(find_smallest_group_brute(weights))

first_comp = [i for i in combinations(weights, 6) if sum(i) == compartment_weight]
# print(len(first_comp))
# valid_first_comp = []

# for config in first_comp:
#     weights_copy = weights.copy()
    
#     for num in config:
#         weights_copy.remove(num)
    
#     for i in range(len(weights_copy)):
#         combos = combinations(weights_copy, i)
        
#         possible = False
        
#         for combo in combos:
#             if sum(combo) == compartment_weight:
#                 valid_first_comp.append(config)
#                 print(f"combo: {combo}")
#                 print(f"config: {config}")
                
#                 for num in combo:
#                     weights_copy.remove(num)
                
#                 print(f"remaining: {weights_copy} \n")
                
#                 possible = True
#                 break
        
#         if possible:
#             break

# print(valid_first_comp)

# #Does not look like there is any difference between them. 
# print(len(first_comp) - len(valid_first_comp))

qes = [math.prod(nums) for nums in first_comp]

# for i in range(len(qes)):
#     print(f"Configuration: {first_comp[i]}")
#     print(f"QE: {qes[i]}")

config = first_comp.pop(qes.index(min(qes)))
print(f"\n--- Ideal Configuration ---")
print(f"Config: {config}")
print(f"QE: {min(qes)} \n")

compartment_weight = total_weight // 4

print(f"The total weight of all packages is still {total_weight}, but each compartment now weighs {compartment_weight}.")

#print(find_smallest_group_brute(weights))

first_comp = [i for i in combinations(weights, 5) if sum(i) == compartment_weight]
qes = [math.prod(nums) for nums in first_comp]
config = first_comp.pop(qes.index(min(qes)))
print(f"\n--- Ideal Configuration ---")
print(f"Config: {config}")
print(f"QE: {min(qes)}")