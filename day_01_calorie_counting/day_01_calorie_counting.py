# input_1 = "input_01.txt"
input_1 = "test_input.txt"

calories = []
elf = []

with open(input_1, mode="r") as text_file:
    while True:
        line = text_file.readline()
        if not line:
            break
        if line == "\n":
            calories.append(elf)
            elf = []
        else:
            elf.append(int(line.strip()))
    calories.append(elf)

# task 1, sum of elf with max calories
max_calories = max((sum(elf) for elf in calories))
print(f"The elf with most calories carried overall \033[4m{max_calories}\033[0m calories.")  # for test input: 24000

# task 2, sum of first three elves with max calories
first_3 = sum(sorted((sum(elf) for elf in calories))[-3:])
print(f"The three elves with most caloric food carried together \033[4m{first_3}\033[0m calories.")
# for test input: 45000
