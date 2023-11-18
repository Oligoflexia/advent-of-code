import re
from utils import helpers

input = helpers.get_input(2016, 7)

def abba_finder(string:str):
    for i in range(len(string) - 3):
        if string[i] == string[i+3] and string[i+1] == string[i+2]:
            if string[i] != string[i +1]: return True
            else: return False

IPs = []
         
for line in input.splitlines():
    IPs.append(line)

def find_valid_IPs():
    valid = []
    
    for ip in IPs:
        valid_bool = True
        hypernet_seq = re.findall(r'\[(.*?)\]', ip)
        
        for seq in hypernet_seq:
            if abba_finder(seq):
                valid_bool = False
        
        sub_line = re.sub(r'\[(.*?)\]', " ", ip)
        
        if not abba_finder(sub_line):
            valid_bool = False
        
        if valid_bool:
            valid.append(ip)
    
    return valid

ips_113 = find_valid_IPs()

print(len(IPs))
cIPs = IPs.copy()
print(len(cIPs))

for ip in IPs:
    if not abba_finder(ip):
        cIPs.remove(ip)

print(len(cIPs))

for ip in IPs:
    hypernet_seq = re.findall(r'\[(.*?)\]', ip)
    
    for seq in hypernet_seq:
        if abba_finder(seq):
            cIPs.remove(ip)

print(len(IPs))
print(len(cIPs))

inconsistencies = list(set(ips_113) - set(cIPs))

print(len(ips_113))

for i in inconsistencies:
    print(i)