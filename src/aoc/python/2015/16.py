from python.utils.input_handler import get_input

input = get_input(2015, 16)

attributes = ['children', 
              'cats', 
              'samoyeds', 
              'pomeranians', 
              'akitas', 
              'vizslas', 
              'goldfish',
              'trees',
              'cars',
              'perfumes']

sues = []

sue_dict = {}

search_sue = {'children': 3, 
              'cats': 7, 
              'samoyeds': 2, 
              'pomeranians': 3, 
              'akitas': 0, 
              'vizslas': 0, 
              'goldfish': 5, 
              'trees': 3, 
              'cars': 2, 
              'perfumes': 1}

for i in range(1, 501):
    sue_dict[i] = {}
    for att in attributes:
        sue_dict[i][att] = -99

for line in input.splitlines():
    data = line.split(" ")
    
    num = int(data[1][:-1])
    att1, val1 = data[2][:-1], int(data[3][:-1])
    att2, val2 = data[4][:-1], int(data[5][:-1])
    att3, val3 = data[6][:-1], int(data[7])
    
    sues.append((search_sue[att1] == val1, search_sue[att2] == val2, search_sue[att3] == val3))
    
    sue_dict[num][att1] = val1
    sue_dict[num][att2] = val2
    sue_dict[num][att3] = val3
    
    
for i, sue in enumerate(sues):
    if sue[0] and sue[1] and sue[2]:
        print(f"The gift was sent by Aunt Sue {i + 1}")

sues_fixed = []

for sue in sue_dict:
    sues_fixed.append(
        (sue_dict[sue]['children'] in [3, -99],
         (sue_dict[sue]['cats'] > 7) or (sue_dict[sue]['cats'] == -99),
         sue_dict[sue]['samoyeds'] in [2, -99],
         sue_dict[sue]['pomeranians'] < 3,
         sue_dict[sue]['akitas'] in [0, -99],
         sue_dict[sue]['vizslas'] in [0, -99],
         sue_dict[sue]['goldfish'] < 5,
         (sue_dict[sue]['trees'] > 3) or (sue_dict[sue]['trees'] == -99),
         sue_dict[sue]['cars'] in [2, -99],
         sue_dict[sue]['perfumes'] in [1, -99],
         )
    )
    
for i, sue in enumerate(sues_fixed):
    if False in sue:
        pass
    else:
        print(f"The Real Aunt Sue was actually #{i + 1}")