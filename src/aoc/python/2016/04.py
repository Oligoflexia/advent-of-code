import re
from heapq import nlargest
from python.utils import input_handler

input = input_handler.get_input(2016, 4)

room_info = []

for line in input.splitlines():
    room_info.append(line.split("-"))

rooms_dict = {}

for i, lst in enumerate(room_info):
    rooms_dict[i] = (str("".join(sorted(list("".join(lst[:-1]))))), lst[-1], "-".join(lst[:-1]))
    
sector_id = []
room_name_dict = {}

for sort_string, numchecksum, string in rooms_dict.values():
    checksum = re.findall(r'\[(.*)\]', numchecksum)[0]
    
    if set(string).issuperset(checksum):
        dic = {}

        for char in sort_string:
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
    
        if "".join(nlargest(5, dic, key=dic.get)) == checksum:
                sector_id.append(int(re.findall(r"\d+", numchecksum)[0]))
                room_name_dict[int(re.findall(r"\d+", numchecksum)[0])] = string

print(sum(sector_id))

def decipher(string:str, num:int) -> str:
    decoded = []
    for char in string:
        if char == "-":
            decoded.append(" ")
        else:
            shifted = ord(char) - 97 + num
            decoded.append(chr((shifted%26) + 97))
    return "".join(decoded)

for key, value in room_name_dict.items():
    if 'north' in decipher(value, key):
        print(f"Room: {decipher(value, key)}, sector: {key}")