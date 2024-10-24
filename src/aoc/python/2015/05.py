from python.utils.input_handler import get_input

input = get_input(2015, 5)

#Returns True if >3 vowels
def check_vowels(input):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for letter in input:
        if letter in vowels.keys():
            vowels[letter]+=1
    
    return(sum(vowels.values()) >= 3)

#Returns True if doubles present
def check_doubles(input):
    if len(input) == 1:
        return False
    
    if input[0] == input[1]:
        return True
    
    return(check_doubles(input[1:]))

#returns false if illegal doublet present
def check_illegal(input):
    illegal = {'ab', 'cd', 'pq', 'xy'}
    
    for i in range(len(input) -1):
        combined = input[i] + input[i+1]
        
        if combined in illegal:
            return False
    
    return True

#Returns True if there is a repeated doublet 
def any_two(input):
    for i in range(len(input) - 1):
        #iterates over every possible doublet of adjacent characters
        combined = input[i] + input[i+1]
        split_list = input.split(combined)
        
        if len(split_list) - 1 >= 2:
            return True
    return False

#Returns True if the character after next is the same
def skip_one(input):
    for i in range(0, len(input) - 2):
        if input[i] == input[i+2]:
            return True
    return False

def count_nice(input):
    nice = 0
    
    for line in input.splitlines():
        if (check_vowels(line) and check_illegal(line) and check_doubles(line)):
            nice+=1
    
    print(f"There are originally {nice} nice strings.")
    return
    
def nicer(input):
    nice = 0
    
    for line in input.splitlines():
        if (skip_one(line) and any_two(line)):
            nice+=1
    
    print(f"There are a revised {nice} nice strings.")
        
count_nice(input)
nicer(input)
