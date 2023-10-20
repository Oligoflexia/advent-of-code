from utils.get_input import get_input

input = get_input(2015, 7)

instructions = {}

for line in input.splitlines():
    commands = line.split(" ")
    instructions[commands[-1]] = {'weight': None, 'instructions': commands[:-2]}

def find_op(list):
    operation = ""
    reserved = {'NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT'}
    for snippet in list:
        if snippet in reserved:
            operation = snippet
    return operation

    
def math(operation, list):
    
    def get_value(item):
        if item.isdigit():
            return int(item)
        else:
            return int(instructions[item]['weight'])
    
    if operation == 'NOT':
        return  ~ get_value(list[1]) & 0xFFFF
    elif operation == 'OR':
        return get_value(list[0]) | get_value(list[2])
    elif operation == 'AND':
        return get_value(list[0]) & get_value(list[2])
    elif operation == 'LSHIFT':
        return get_value(list[0]) << int(list[2])
    elif operation == 'RSHIFT':
        return get_value(list[0]) >> int(list[2])
    elif list[0] in instructions.keys():
        return int(instructions[list[0]]['weight'])
    else:
        return get_value(list[0])
    
def solver(string):
    if instructions[string]['weight'] is not None:
        return instructions[string]['weight']
    
    for item in instructions[string]['instructions']:
        if item in instructions.keys():
            solver(item)
    
    operation = find_op(instructions[string]['instructions'])
    instructions[string]['weight'] = math(operation, instructions[string]['instructions'])
    
    return instructions[string]['weight']

        
print(solver('a'))
    
        
        
        
    
            
        
