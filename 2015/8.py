from utils.get_input import get_input

input = get_input(2015, 8)

literal = 0
mem = 0
modified = []

for line in input.splitlines():
    literal += len(line)
    
    #running into issues becuase iterating over a modified string. Need to work on a copy. 
    for index, character in enumerate(line[:-1]):
        if character == '\\':
            if line[index + 1] == '\\':
                line = line.replace('\\\\', '$', 1)
                print(line)
            elif line[index + 1] == "\\\"":
                line = line.replace('\\\"', '$', 1)
                print(line)
            elif line[index + 1] == "x":
                #convert - think about this one
                pattern = f"\\x{line[index+2]}{line[index+3]}"
                line = line.replace(pattern, '$', 1)
                print(line)


         
        
            
