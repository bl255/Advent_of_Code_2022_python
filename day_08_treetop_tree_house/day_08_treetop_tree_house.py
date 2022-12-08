import numpy as np

input_1 = "input_08.txt"
# input_1 = "test_input.txt"

with open(input_1, mode="r") as text_file:
    forest = np.array([list(map(int, line)) for line in text_file.read().splitlines()])


# TASK 1

check_hidden = np.zeros(forest.shape, dtype=int)

for x in range(1, forest.shape[0] - 1):
    for y in range(1, forest.shape[1] - 1):
        check_hidden[x, y] = all([forest[x, y] <= max(forest[:x, y]),
                                  forest[x, y] <= max(forest[x + 1:, y]),
                                  forest[x, y] <= max(forest[x, :y]),
                                  forest[x, y] <= max(forest[x, y + 1:])])


print(forest.shape[0] * forest.shape[1] - check_hidden.sum())  # my input 1851


# TASK 2

def np_see_trees(num, array):
    rule = num <= array
    if array.shape[0] == 0:
        return 0
    else:
        if np.argmax(rule) == 0 and num > max(array):
            return array.shape[0]
        return np.argmax(rule) + 1


check_see_trees = np.zeros(forest.shape, dtype=int)

for x in range(forest.shape[0]):
    for y in range(forest.shape[1]):
        u, l, d, r = forest[:x, y][::-1], forest[x, :y][::-1], forest[x + 1:, y], forest[x, y + 1:]
        check_see_trees[x, y] = np_see_trees(forest[x, y], u) * np_see_trees(forest[x, y], l) *\
            np_see_trees(forest[x, y], d) * np_see_trees(forest[x, y], r)

print(np.amax(check_see_trees))
