from string import ascii_lowercase, ascii_uppercase

# input_1 = "input_03.txt"
input_1 = "test_input.txt"

BIGSTRING = ascii_lowercase + ascii_uppercase

with open(input_1, mode="r") as text_file:
    rucksacks = [line.strip() for line in text_file.readlines()]

# TASK 1
duplicated = (tuple(set(rs[:int(len(rs)/2)]).intersection(set(rs[int(len(rs)/2):]))) for rs in rucksacks)
val_dupl = (BIGSTRING.index(item[0]) + 1 for item in duplicated)
important_sum = sum(val_dupl)
print(important_sum)
# for test input 157

#TASK 2:
number = 0
for ind in range(0, len(rucksacks), 3):
    number += BIGSTRING.index(
        tuple(set(rucksacks[ind]).intersection(set(rucksacks[ind + 1]), set(rucksacks[ind + 2])))[0]) + 1

print(number)
# for test input 70