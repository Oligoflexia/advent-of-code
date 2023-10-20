from utils.get_input import get_input
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

for line in input.splitlines():
    formatted = repr(line)[1:-1]
    exp_lit += len(formatted)
    print(f"{formatted} ::: lit: +{len(formatted)} ::: total_exp_lit: {exp_lit}")
    print("\n")
  
print(f"The difference between the # of original vs modified literal chars is: {exp_lit-lit}")

print(r'"aaa\"aaa"')
print(len(r'"aaa\"aaa"'))
print("\n")

print(repr(r'"aaa\"aaa"'))
print(len(repr(r'"aaa\"aaa"')))
print("\n")
    
    