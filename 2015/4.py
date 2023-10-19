import hashlib
from utils.get_input import get_input

input = get_input(2015, 4)

test = 'abcdef609043'
test1 = 'pqrstuv1048970'

def generate_md5(input):
    hash = hashlib.md5()
    hash.update(input.encode('utf-8'))
    return hash.hexdigest()


def brute_force(input, zeros):
    n = 1
    
    while True:
        hash = generate_md5(input + str(n))

        if hash[:zeros] == '0' * zeros:
            print(f"The smallest possible integer is {n}.")
            return str(n)
        n+=1


five = brute_force(input, 5)
print(f"The generated hash is {generate_md5(input + five)}.")

six = brute_force(input, 6)
print(f"The generated hash is {generate_md5(input + six)}.")

