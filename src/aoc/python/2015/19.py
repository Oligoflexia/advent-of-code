import re
from python.utils.input_handler import get_input

input = get_input(2015, 19)

query_str  = ""
replacements = {}

for line in input.splitlines()[:-2]:
    original, _, replaced = line.split(" ")
    
    if original not in replacements:
        replacements[original] = []
        replacements[original].append(replaced)
    else: replacements[original].append(replaced)

query_str += input.splitlines()[-1:][0]

def replacer(instructions:tuple, str=query_str) -> list:
    created_molecules = []
    
    inds = [match.start() for match in re.finditer(instructions[0], str)]
    
    for element in inds:
        temp_s = str[:element] + instructions[1] + str[element+len(instructions[0]):]
        created_molecules.append(temp_s)
    
    return created_molecules

def solver() -> int:
    unique_molecules = set()
    
    for key, value in replacements.items():
        for element in value:
            molecules = replacer((key, element))
        
            for molecule in molecules:
                unique_molecules.add(molecule)
    
    return(len(unique_molecules))

ans = solver()

print(f"The instruction set yields {ans} unique molecules from the starting medical molecule")

# Each substitution takes 1 element -> 2 or more.
# If we assume every substitution added 2 elements, then going backwards will require total_element - 1 steps
# Let X be any element that is not e, Rn, Ar, or Y
# X -> XX and when going backward (XX)XX -> (YX)X -> (ZX) -> X
# This should be the theoretical maximum number of steps

elements = len(re.findall(r'[A-Z][a-z]?', query_str))
# 292 total elements - 1 = 291

# Notice that Rn...Ar substitutions always appear together. There is no Ar added without a corresponding Rn.
# These are also final. Once an Rn or Ar is added there is no rule to replace it.
# Each one of these substitutions goes from X -> X Rn X Ar, for 2 unaccounted elements per substitution/pair
# so we subtract 2 * #Rn...Ar pairs from the maximum steps 

#sanity check
if query_str.count('Ar') == query_str.count('Rn'):
    pairs = query_str.count('Ar')
    # 36 * 2 = 72

# Notice that the Rn ... Ar substitution can also introduce a Y character
# In this case the substitution becomes X -> X Rn X Y X Ar or X -> X Rn X Y X Y X Ar
# The Rn and Ar is already accounted for, as is the first 2 Xs. 
# Every Y character introduces another X character however.
# We subtract double the number of Ys to deal with this

ys = query_str.count('Y')
# 6 * 2 = 12

def minimum_steps(e, RnAr, Y) -> int:
    return e - 1 - (2 * RnAr) - (2 * Y)

print(f"The minimum number of substitutions required to reach 'e' from the medicine molecule is {minimum_steps(elements, pairs, ys)}")
