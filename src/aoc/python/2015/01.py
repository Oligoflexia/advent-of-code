from utils import input_formatter

StringInput = input_formatter.StringInput(1, 2015)
input_str = StringInput.input

# Time complexity: O(n)
#
#   The function takes a string s, of length n, and iterates through it.
# At each iteration it performs a single equality check and addition
# operation. It terminates at the end of the string.
#
# Space complexity: O(1)
#
#   A fixed number of variables are created and updated trhoughout.
final_floor = lambda s: sum(1 if c == "(" else -1 for c in s)


# Time complexity O(n)
#
#   In the worst case, the function will iterate until the end of the
# input string.
#
# Space complexity O(1)
#
#   The generator expression makes values one at a time unlike a list comp.
# sum is a running total and does not increase in size depending on n.
def when_basement(input_str: str) -> int:
    floor = 0
    for i, char in enumerate(input_str, 1):
        floor += 1 if char == "(" else -1
        if floor < 0:
            return i
    return -1


print(final_floor(input_str))
print(when_basement(input_str))
