from utils import helpers

input = helpers.get_input(2016, 6)

codewords = []
counts = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7:{}}

for line in input.splitlines():
    codewords.append(line)
    
for word in codewords:
    for index, char in enumerate(word):
        if char not in counts[index]:
            counts[index][char] = 0
        counts[index][char] += 1

enc_message = []
for dic in counts.values():
    enc_message.append(max(dic, key= dic.get))

print("".join(enc_message))

enc_message = []
for dic in counts.values():
    enc_message.append(min(dic, key= dic.get))

print("".join(enc_message))
