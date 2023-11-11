from utils.helpers import get_input


input = get_input(2015, 11)

trips = set()
illegal = {'i', 'o', 'l'}

for i in range(97, 122):
    trips.add(f"{chr(i)}{chr(i+1)}{chr(i+2)}")

def increment(s:str) -> str:
    ascii = [ord(x) for x in s]
    
    i = len(ascii) - 1
    
    while i > 0:
        if ascii[i] == 122:
            ascii[i] = 97
            i -= 1
        else:
            ascii[i] += 1
            break
    return ''.join(chr(n) for n in ascii)
    
def hasStraight(s:str) -> bool:
    straight = False
    for ind, c in enumerate(s[0:-2]):
        if f"{c.lower()}{s[ind+1].lower()}{s[ind+2].lower()}" in trips:
            straight = True
    return straight

def isNotIllegal(s:str) -> bool:
    not_illegal = True
    for c in s:
        if c in illegal:
            not_illegal = False
    return not_illegal

def hasDoubles(s:str) -> bool:
    pairs = []
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            pairs.append(s[i:i + 2])
            i += 2
        else:
            i += 1
    return len(pairs) >= 2

def solve(s:str) -> str:
    while True:
        if hasDoubles(s) and hasStraight(s) and isNotIllegal(s):
            break
        s = increment(s)
    return s

ans = solve(input)

print(f"Santa's next password should be:{ans}")

ans = increment(ans)

print(f"Santa's next new password should be:{solve(ans)}")