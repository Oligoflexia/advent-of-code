import re
from utils.get_input import get_input

input = get_input(2015, 25)
row, column = tuple(re.findall(r'\d+', input))
row = int(row)
column = int(column)

def calculate_moves(row:int, column:int) -> int:
    val=1
    for i in range(row):
        val += i
    
    for i in range(1, column):
        val += row + i
    return val

def exponentiation_by_squaring(base, exponent, mod):
    if mod == 1:
        return 0
    
    result = 1
    base = base % mod
    
    while exponent > 0:
        if exponent % 2 == 1:
           result = (result * base) % mod
        exponent = exponent >> 1  # Shift right, equivalent to exponent // 2
        base = (base * base) % mod
        
    return result

def find_code(row:int, column:int) -> int:
    val = calculate_moves(row, column) - 1
    
    code = (20151125 * exponentiation_by_squaring(252533, val, 33554393)) % 33554393
    
    return code

print(find_code(row, column))
