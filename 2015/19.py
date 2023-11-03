import re
from utils.get_input import get_input

input = get_input(2015, 19)

query_str  = ""
replacements = {}

for line in input.splitlines()[:-2]:
    original, _, replaced = line.split(" ")
    
    if replaced in replacements:
        raise ValueError("Patterns are not unique")
    replacements[replaced] = original

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
    
    for key in replacements:
        molecules = replacer((replacements[key], key))
        
        for molecule in molecules:
            unique_molecules.add(molecule)
    
    return(len(unique_molecules))

ans = solver()

print(f"The instruction set yields {ans} unique molecules from the starting medical molecule")

#Takes a query string and returns the shortest string formed in 1 step
def backwards(pattern:str) -> str:
    molecules = []
    shortest = ""
    
    for patt in [key for key in replacements if key in pattern]:
        mols = replacer((patt, replacements[patt]), pattern)

        for mol in mols:
            molecules.append(mol)
    
    min = float('inf')
    for mol in molecules:
        if len(mol) < min:
            min = len(mol)
            shortest = mol
    
    return shortest

def back_solver(num:int, pattern:str) -> str:
    patt = pattern
    
    for i in range(num):
        patt = backwards(patt)
    
    return patt

print(back_solver(201, query_str))
    
    

        
        
    
    
    