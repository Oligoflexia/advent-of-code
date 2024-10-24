from python.utils.input_handler import get_input


input = get_input(2015, 23)

tape = []

for line in input.splitlines():
    instructions = line.split(" ")
    
    if instructions[0] == 'jio' or instructions[0] == 'jie':
        instructions[1] = instructions[1][:-1]
    
    tape.append((instructions[0], instructions[1:]))
    
for instruction in tape:
    print(instruction)

register = {'a': 1, 'b': 0}

def next_index(instruction:tuple, index:int):
    global tape
    global register
    
    match instruction[0]:
        case 'hlf':
            register[instruction[1][0]] = register[instruction[1][0]] // 2
        case 'tpl':
            register[instruction[1][0]] = register[instruction[1][0]] * 3
        case 'inc':
            register[instruction[1][0]] = register[instruction[1][0]] + 1
    
    if instruction[0] in ['hlf', 'tpl', 'inc']:
        return index + 1
    elif instruction[0] == 'jmp':
        return index+int(instruction[1][0])
    elif instruction[0] == 'jie':
        if register[instruction[1][0]] % 2 == 0:
            return index + int(instruction[1][1])
        else: return index + 1
    elif instruction[0] == 'jio':
        if register[instruction[1][0]] == 1:
            return index + int(instruction[1][1])
        else: return index + 1
    

i = 0
while True:
    try:
        print(tape[i])
        
        i = next_index(tape[i], i)

    except IndexError as e:
        print(f"b: {register['b']}")
        break