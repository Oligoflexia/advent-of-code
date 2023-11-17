from utils.helpers import get_input

input = get_input(2016, 4)

room_info = []

for line in input.splitlines():
    room_info.append(line.split("-"))

rooms_dict = {}

for i, lst in enumerate(room_info):
    rooms_dict[i] = (str("".join(sorted(list("".join(lst[:-1]))))), lst[-1])

print(rooms_dict)