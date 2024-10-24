import re
from python.utils.input_handler import get_input

input = get_input(2016, 3)

side_lengths = []
valid_triangles = 0

for line in input.splitlines():    
    nums = [int(i) for i in re.findall(r'\d+', line)]
    side_lengths.append(nums)
    
    all_sides = sum(nums)
    b1 = all_sides - nums[0] > nums[0]
    b2 = all_sides - nums[1] > nums[1]
    b3 = all_sides - nums[2] > nums[2]
    
    if b1 and b2 and b3:
        valid_triangles += 1

print(valid_triangles)

valid_triangles = 0

for i in range(0, len(side_lengths), 3):
    tri = side_lengths[i:i+3]
    
    sum_a = sum([tri[0][0], tri[1][0], tri[2][0]])
    sum_b = sum([tri[0][1], tri[1][1], tri[2][1]])
    sum_c = sum([tri[0][2], tri[1][2], tri[2][2]])

    a1 = sum_a - tri[0][0] > tri[0][0]
    a2 = sum_a - tri[1][0] > tri[1][0]
    a3 = sum_a - tri[2][0] > tri[2][0]

    if a1 and a2 and a3:
        valid_triangles += 1

    a1 = sum_b - tri[0][1] > tri[0][1]
    a2 = sum_b - tri[1][1] > tri[1][1]
    a3 = sum_b - tri[2][1] > tri[2][1]

    if a1 and a2 and a3:
        valid_triangles += 1

    a1 = sum_c - tri[0][2] > tri[0][2]
    a2 = sum_c - tri[1][2] > tri[1][2]
    a3 = sum_c - tri[2][2] > tri[2][2]

    if a1 and a2 and a3:
        valid_triangles += 1

print(valid_triangles)