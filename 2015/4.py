import hashlib

test = 'abcdef609043'
test1 = 'pqrstuv1048970'

input = 'yzbqklnj'

def generate_md5(input):
    
    hash = hashlib.md5()
    
    hash.update(input.encode('utf-8'))
    
    return hash.hexdigest()


def brute_force(input):
    n = 1
    
    while True:
        hash = generate_md5(input + str(n))

        if hash[:6] == '000000':
            print(n)
            break
        n+=1


#brute_force(input)
print(generate_md5(input + str(9962624)))