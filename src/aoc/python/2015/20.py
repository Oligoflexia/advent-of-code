from python.utils.input_handler import get_input

input = int(get_input(2015, 20))

def lowest_house(bound:int) -> int:
    houses = [0] * (bound // 10)
    for elf in range(1, len(houses)):
        for house in range(elf, len(houses), elf):
            houses[house] += elf * 10
        if houses[elf] >= bound:
            return elf

print(lowest_house(input))

# add a new bound which checks if factor * 50 is less than the current number
def lowest_house_restricted(bound:int) -> int:
    houses = [0] * (bound // 10)
    for elf in range(1, len(houses)):
        for house in range(elf, min(elf * 50, len(houses)), elf):
            houses[house] += elf * 11
        if houses[elf] >= bound:
            return elf


print(lowest_house_restricted(input))