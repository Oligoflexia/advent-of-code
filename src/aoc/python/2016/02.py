from python.utils.input_handler import get_input

input = get_input(2016, 2)

keypad = {(0, 2): 1, (1, 2): 2, (2, 2): 3,
          (0, 1): 4, (1, 1): 5, (2, 1): 6,
          (0, 0): 7, (1, 0): 8, (2, 0): 9}

def key_presser(instructions:str, start:[int, int]) -> int:
    for char in instructions:
        match char:
            case 'U':
                if start[1] + 1 > 2:
                    pass
                else: start[1] += 1
            case 'D':
                if start[1] - 1 < 0:
                    pass
                else: start[1] -= 1
            case 'L':
                if start[0] - 1 < 0:
                    pass
                else: start[0] -= 1
            case 'R':
                if start[0] + 1 > 2:
                    pass
                else: start[0] += 1
    return start

def solve(input_str:str, start:[int, int]) -> [int]:
    keys = []
    
    for line in input_str.splitlines():
        num_key = key_presser(line, start)
        keys.append(keypad[tuple(num_key)])
    
    return keys

print(solve(input, [1, 1]))

fd_keypad = {(2, 4): 1,
             (1, 3): 2, (2, 3): 3, (3, 3): 4,
             (0, 2): 5, (1, 2): 6, (2, 2): 7, (3, 2): 8, (4, 2): 9,
             (1, 1): 'A', (2, 1): 'B', (3, 1): 'C',
             (2, 0): 'D'}

def new_key_presser(instructions:str, start:[int, int]) -> int:
    for char in instructions:
        match char:
            case 'U':
                if (start[0], start[1] + 1) not in fd_keypad:
                    pass
                else: start[1] += 1
            case 'D':
                if (start[0], start[1] - 1) not in fd_keypad:
                    pass
                else: start[1] -= 1
            case 'L':
                if (start[0] - 1, start[1]) not in fd_keypad:
                    pass
                else: start[0] -= 1
            case 'R':
                if (start[0] + 1, start[1]) not in fd_keypad:
                    pass
                else: start[0] += 1
    return start

def new_solve(input_str:str, start:[int, int]) -> [int]:
    keys = []
    
    for line in input_str.splitlines():
        num_key = new_key_presser(line, start)
        keys.append(fd_keypad[tuple(num_key)])
    
    return keys

print(new_solve(input, [0, 2]))