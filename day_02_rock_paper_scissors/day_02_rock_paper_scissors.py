import numpy as np

input_1 = "input_02.txt"
# input_1 = "test_input.txt"

# A = 1, B = 2, C = 3
# A > B, B > C, C > A

RULES_0 = {"X": "A", "Y": "B", "Z": "C"}

RULES = {"AB": 6 + 2, "BC": 6 + 3, "CA": 6 + 1,
         "AA": 3 + 1, "BB": 3 + 2, "CC": 3 + 3,
         "BA": 0 + 1, "CB": 0 + 2, "AC": 0 + 3}

RULES_2 = {"AZ": 6 + 2, "BZ": 6 + 3, "CZ": 6 + 1,
           "AY": 3 + 1, "BY": 3 + 2, "CY": 3 + 3,
           "BX": 0 + 1, "CX": 0 + 2, "AX": 0 + 3}

with open(input_1, mode="r") as text_file:
    match = np.array([line.strip().split(" ") for line in text_file.readlines()])

elf = match[:, 0]
you = match[:, 1]


# DECRYPTION = ({"X": "A", "Y": "B", "Z": "C"}, {"X": "C", "Y": "A", "Z": "B"}, {"X": "B", "Y": "C", "Z": "A"},
#               {"X": "A", "Y": "C", "Z": "B"}, {"X": "C", "Y": "B", "Z": "A"}, {"X": "B", "Y": "A", "Z": "C"})
#
# for x in range(len(DECRYPTION)):
#     you_d = np.vectorize(DECRYPTION[x].__getitem__)(you)
#     combined_choices = np.core.defchararray.add(elf, you_d)
#     scores = np.vectorize(RULES.__getitem__)(combined_choices)
#     print(f"variation {x}: {sum(scores)}")

# above commented out is not necessary, if you know the decryption

# TASK 1
you_d = np.vectorize(RULES_0.__getitem__)(you)
combined_choices = np.core.defchararray.add(elf, you_d)
scores = np.vectorize(RULES.__getitem__)(combined_choices)

# TASK 2
combined_choices_2 = np.core.defchararray.add(elf, you)
scores_2 = np.vectorize(RULES_2.__getitem__)(combined_choices_2)


print(f"Task 1: {sum(scores)}")  # result for my input 12156
print(f"Task 2: {sum(scores_2)}")  # result for my input 10835

# IMPORTANT NOTE: this code could be improved by getting match values in the form of "AX", and then applying vectorized
# directly on the match array, choosing the appropriate dictionary, but because of gradual evolution of the script
# (i.e. me not understanding the instructions entirely right while starting to write this), I decided to keep some odd
# parts which would enable to change first decryption and try different variants
