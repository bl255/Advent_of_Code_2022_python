import numpy as np

input_1 = "input_08.txt"
# input_1 = "test_input.txt"

with open(input_1, mode="r") as text_file:
    forest = np.array([list(map(int, line)) for line in text_file.read().splitlines()])


def seen_trees(num, array):
    if np.array(array >= num).any():
        return int(np.argwhere(array >= num)[0]) + 1
    return array.size


visible_trees = np.zeros(forest.shape, dtype=int) + 1  # at the beginning filled with 1, border trees are visible
sum_seen_trees = np.zeros(forest.shape, dtype=int)

# the following solution would not work if border points are considered, because of empty arrays

for x in range(1, forest.shape[0] - 1):
    for y in range(1, forest.shape[0] - 1):
        u, l, d, r = forest[:x, y][::-1], forest[x, :y][::-1], forest[x + 1:, y], forest[x, y + 1:]
        visible_trees[x, y] = any([forest[x, y] > max(u), forest[x, y] > max(l),
                                  forest[x, y] > max(d), forest[x, y] > max(r)])

        sum_seen_trees[x, y] = seen_trees(forest[x, y], u) * seen_trees(forest[x, y], l) *\
            seen_trees(forest[x, y], d) * seen_trees(forest[x, y], r)


print(visible_trees.sum())  # task 1, for my input 1851
print(np.amax(sum_seen_trees))  # task 2, for my input 574080
