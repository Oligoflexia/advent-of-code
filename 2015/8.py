from utils.get_input import get_input

input = get_input(2015, 8)

literal = 0
mem = 0
modified = []

for line in input.splitlines():
    literal += len(repr(line))
    
def string_iterator(string:str, is_literal=False) -> str:
    if not is_literal:
        string = repr(string)[1:-1]
    
    new_string = ''
    skip = False
    
    for index, char in enumerate(string[:-1]):
        if skip:
            skip = False
            continue
        next_char = string[index + 1]
        if char == '\\' and next_char == '\\':
            new_string += '$'
            skip = True
        else:
            new_string += char
            
    new_string += string[-1] if not skip else ''
    print(new_string)

    if new_string != string:
        return string_iterator(new_string, is_literal=True)
    else:
        return new_string

result = string_iterator("byc\x9dyxuafof\\\xa6uf\\axfozomj\\olh\x6a")
print("Final result:", result)


