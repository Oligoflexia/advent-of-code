from utils.get_input import get_input

input = get_input(2015, 8)

for line in input.splitlines():
    literal = len(line)
    
    total = 0
    
    for index, character in enumerate(line):
        if character == '\\':
            if line[index + 1] == '\\':
                pre = line[:index]
                post = line[index + 2]
                new = pre + ' ' +post
                print(len(new))
                total += (literal - len(new))
            elif line[index + 1] == "\"":
                pre = line[:index]
                post = line[index + 2]
                new = pre + ' ' + post
                print(len(new))
                total += (literal - len(new))
            else:
                pre = line[:index]
                post = line[index + 4]
                new = pre + ' ' +post
                print(len(new))
                total += (literal - len(new))

            
