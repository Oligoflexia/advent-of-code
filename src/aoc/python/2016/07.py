import re
from python.utils import input_handler

input = input_handler.get_input(2016, 7)

def abba_finder(string:str):
    for i in range(len(string) - 3):
        if string[i] == string[i+3] and string[i+1] == string[i+2]:
            if string[i] != string[i +1]: return True
            else: return False
    return False

def aba_finder(string:str):
    ABAs = []
    for i in range(len(string) - 2):
        if string[i] == string[i+2] and string[i] != string[i+1]:
            ABAs.append(string[i:i+3])
    return ABAs

IPs = []
         
for line in input.splitlines():
    IPs.append(line)

cIPs = IPs.copy()

for ip in IPs:
    if not abba_finder(ip):
        cIPs.remove(ip)

for ip in IPs:
    hypernet_seq = re.findall(r'\[(.*?)\]', ip)
    
    for seq in hypernet_seq:
        if abba_finder(seq):
            cIPs.remove(ip)

print(len(cIPs))

valid = []

for ip in IPs:
    hypernet_seq = re.findall(r'\[(.*?)\]', ip)
    
    for seq in hypernet_seq:
        ABAs = aba_finder(seq)
        
        for char in ABAs:
            pattern = char[1] + char[0] + char[1]
            if pattern in re.sub(r"\[.*?\]", " ", ip):
                valid.append(ip)
                break
            
        if ip in valid:
            break

print(len(valid))
    