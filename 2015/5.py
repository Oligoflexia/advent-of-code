from utils.get_input import get_input

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

def check_illegal(input):
    illegal = {'ab', 'cd', 'pq', 'xy'}
    
    for i in range(len(input) -1):
        combined = input[i] + input[i+1]
        
        if combined in illegal:
            return False
    
    return True

def count_nice(input):
    nice = 0
    
    for line in input.splitlines():
        if (check_vowels(line) and check_illegal(line) and check_doubles(line)):
            nice+=1
    
    print(f"There are originally {nice} nice strings.")
        
count_nice(input)