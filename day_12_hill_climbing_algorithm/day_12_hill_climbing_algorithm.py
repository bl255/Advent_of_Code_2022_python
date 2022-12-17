# https://www.youtube.com/watch?v=pLElbKBc4RU
# https://www.youtube.com/watch?v=VnTlW572Sc4
# https://www.youtube.com/watch?v=EFg3u_E6eHU

import numpy as np
from string import ascii_letters

# input_1 = "input_12.txt"
input_1 = "test_input.txt"

# print(ascii_letters.index("S"), ascii_letters.index("E"))  # 44, 30

w_nod_distance = 1
d_shortest_se = None
permanent_nodes = None
temporary_nodes = None

with open(input_1, mode="r") as text_file:
    terrain = np.array([[ascii_letters.index(letter)
                         for letter in line] for line in text_file.read().splitlines()], dtype=int)


def near_func(pos, ter=terrain):
    x = pos[0]
    y = pos[1]
    possible = ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y))
    return tuple([p for p in possible if all([p[0] >= 0, p[1] >= 0, (ter[p] - ter[pos]) < 2])])


#end correction
terrain[terrain == 30] = -1
#
nodes_tuple = tuple(zip(np.indices(terrain.shape)[0].flatten(), np.indices(terrain.shape)[1].flatten()))
nodes = np.empty(terrain.size, dtype=object)
nodes[:] = nodes_tuple
nodes = np.reshape(nodes, terrain.shape)

start = nodes[terrain == 44][0]
end = nodes[terrain == -1][0]

unexplored = np.ones(terrain.shape, dtype=bool)
distances = np.ones(terrain.shape, dtype=int) * np.inf

distances[start] = 0  # setting start
unexplored[start] = 0

node = start
# while node != nodes[end]:
for x in range(1):
    choices = tuple(set(near_func(node)) & set(nodes[unexplored]))
    print("choices", choices)
    distances[choices] = distances[node] + 1
    choice_id = near_func(node)[int(np.argwhere(distances[near_func(node)] == min(distances[near_func(node)]))[0])]
    print("choice id", choice_id)
    unexplored[choice_id] = 0
    node = choice_id

dva = (0, 1)
print(distances)
# print(near_func((0, 1)))
print()
choices = ((1, 1), (0, 2))
distances[choices] = 8
print(distances[(1, 1), (0, 2)])


# nodes, distances, was_explored
# update time estimates
# choose next node









