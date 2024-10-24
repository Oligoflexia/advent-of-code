from utils.input_formatter import SplitStringInput
import re

InputObject, input_str_list = SplitStringInput.return_input(1, 2023)


def sum_number_combos(str_list):
    t_num = 0

    for line in str_list:
        num_list = re.findall(r"\d", line)
        num = num_list[0] + num_list[-1]

        t_num += int(num)
    return t_num


print(sum_number_combos(input_str_list))

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def sum_with_string(str_list):
    pattern = r"(one|two|three|four|five|six|seven|eight|nine|\d)"
    all_num_list = []

    for line in str_list:
        num_list = [
            match.group()
            for start in range(len(line))
            for match in [re.match(pattern, line[start:])]
            if match
        ]

        first = num_list[0]
        last = num_list[-1]

        if first in nums:
            first = nums[first]
        if last in nums:
            last = nums[last]

        num = str(first) + str(last)
        all_num_list.append(int(num))
    return sum(all_num_list)


print(sum_with_string(input_str_list))
