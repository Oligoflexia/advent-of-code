from utils.helpers import get_input

input = get_input(2015, 10)

def stepper(input:str) -> str:
    lengths = []
    c = 1
    for i, d in enumerate(input[:-1]):
        if d == input[i+1]:
            c += 1
        else:
            lengths.append(c)
            lengths.append(input[i])
            c = 1

    lengths.append(c)
    lengths.append(input[-1])

    s = ""

    for d in map(str, lengths):
        s += d
    
    return s

def it_num(n:int, s:str) -> str:
    if n == 0:
        return s
    new = stepper(s)
    return it_num(n-1, new)
        
print(f"The length of the number is: {len(str(it_num(50, input)))}")