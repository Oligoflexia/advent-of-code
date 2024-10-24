import hashlib
from python.utils import input_handler

input = input_handler.get_input(2016, 5)

def hash_finder(start_str:str):
    password = []
    i = 0
    while len(password) < 8:
        cur_str = start_str + str(i)
        hex_hash = hashlib.md5(cur_str.encode()).hexdigest()
        if hex_hash[:5] == "00000":
            password.append(str(hex_hash[5]))
        i += 1
    return "".join(password)

print(hash_finder(input))

def complex_hash_finder(start_str:str):
    password = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None}
    i = 0
    n = 0
    while n < 8:
        cur_str = start_str + str(i)
        hex_hash = hashlib.md5(cur_str.encode()).hexdigest()
        if hex_hash[:5] == "00000" and hex_hash[5].isdigit():
            if int(hex_hash[5]) in password:
                if password[int(hex_hash[5])] is None:
                    password[int(hex_hash[5])] = str(hex_hash[6])
                    n += 1
        i += 1
    return "".join(password.values())

print(complex_hash_finder(input))
