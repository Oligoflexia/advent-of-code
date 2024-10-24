from python.utils.input_handler import get_input
import ast

input = get_input(2015, 8)

lit = 0
mem = 0
exp_lit = 0


for line in input.splitlines():
    lit += len(line)
    print(f"{line} ::: lit: +{len(line)} ::: total_lit: {lit}")
    
    mem += len(ast.literal_eval(line))
    print(f"{ast.literal_eval(line)} ::: mem: +{len(ast.literal_eval(line))} ::: total_mem: {mem}")
    print("\n")

print(f"The difference between the # of literal chars and those saved in mem is {lit-mem}")

def go_up(line):
    charlist = list(line)
    insert_idx = []
    
    for index, char in enumerate(charlist):
        if char == '\\' or char == '"':
            insert_idx.append(index)
    
    print(insert_idx)
    
    def insert_multiple(lst, char, index):
        for index in sorted(index, reverse=True):
            lst.insert(index, char)
    
    insert_multiple(charlist, '\\', insert_idx)
    
    insert_multiple(charlist, '"', [0, 9])
    
    global exp_lit 
    exp_lit += len(charlist)
    
    

for line in input.splitlines():
    go_up(line)        

print(exp_lit)

print(f"The difference is {exp_lit - lit}!")

