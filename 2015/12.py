import re
from utils.helpers import get_input

input = get_input(2015, 12)

def str_sum(s:str) -> int:
    pattern = r'-?\d+'
    nums = re.findall(pattern, s)
    
    return sum(int(x) for x in nums)

print(f"The sum of all the integers in the input is: {str_sum(input)}")

def no_red(input_str:str) -> str:
    curly_stack = []
    square_stack = []
    pairs = {}

    for index, char in enumerate(input_str):
        if char == '{':
            curly_stack.append(index)
        elif char == '[':
            square_stack.append(index)
        elif char == '}':
            if len(curly_stack) == 0:
                print(f"unclosed curly bracket at index: {index}")
            else:
                pairs[curly_stack.pop()] = (index, 'curly')
        elif char == ']':
            if len(square_stack) == 0:
                print(f"unclosed square bracket at index: {index}")
            else:
                pairs[square_stack.pop()] = (index, 'square')

    l = list(input_str)

    for key, (end, bracket) in pairs.items():
        substring = input_str[key:end+1]
        if 'red' in substring:
            if bracket == 'square':
                new_substring = substring.replace('red', '$$$')
                l[key:end+1] = list(new_substring)
                input_str = "".join(l)
            elif bracket == 'curly':
                new_substring = "$" * (len(substring) - 2)
                l[key +1:end] = list(new_substring)
                input_str = "".join(l)

    return "".join(l)

print(f"The sum of all the integers in the input is: {str_sum(no_red(input))}")