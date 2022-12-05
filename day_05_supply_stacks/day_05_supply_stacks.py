from string import ascii_uppercase, digits
import copy
import re

input_1 = "input_05.txt"
# input_1 = "test_input.txt"

with open(input_1, mode="r") as text_file:
    all_i = (line for line in text_file.read().splitlines())

raw_crates, col_hints, m_hints = [], [], []

for line in all_i:
    if line == "":
        break
    elif len(set(ascii_uppercase) & set(line)):
        raw_crates += [(num, let) for num, let in enumerate(line) if let in ascii_uppercase]
    else:
        col_hints += [num for num, let in enumerate(line) if let in digits]
        m_hints += [let for num, let in enumerate(line) if let in digits]


all_crates = [[] for hint in col_hints]
for crate in raw_crates:
    all_crates[col_hints.index(crate[0])].append(crate[1])

better_crates = copy.deepcopy(all_crates)

# using all remaining lines of all_i generator
for line in all_i:
    instr = re.findall(r"\d+", line)
    amount = int(instr[0])

    # task 1:
    for move in range(amount):
        moved_t1 = list(all_crates[m_hints.index(instr[1])].pop(0))
        all_crates[m_hints.index(instr[2])] = moved_t1 + all_crates[m_hints.index(instr[2])]

    # task 2:
    moved_t2 = better_crates[m_hints.index(instr[1])][:amount]
    better_crates[m_hints.index(instr[2])] = moved_t2 + better_crates[m_hints.index(instr[2])]
    better_crates[m_hints.index(instr[1])] = better_crates[m_hints.index(instr[1])][amount:]

# result task 1:
print("".join((crate[0] for crate in all_crates)))
# for my input TLFGBZHCN

# result task 2:
print("".join((crate[0] for crate in better_crates)))
# for my input TLFGBZHCN
