import re
from utils.get_input import get_input

input = get_input(2015, 12)

def str_sum(s:str) -> int:
    pattern = r'-?\d+'
    nums = re.findall(pattern, s)
    
    return sum(int(x) for x in nums)

print(f"The sum of all the integers in the input is: {str_sum(input)}")

def no_red(s:str) -> int:
    pattern = r'{.*?red.*?}'
    
    new = re.sub(pattern, "", s)
    
    print(new)
    
    return str_sum(new)

print(f"The sum of all the integers in the input is: {no_red(input)}")