import numpy as np
import matplotlib.pyplot as plt

# input_1 = "input_14.txt"
input_1 = "test_input.txt"


def good_y(xpos, y_limit, taken_list):
    return min([p[1] for p in taken_list if (p[0] == xpos and p[1] > y_limit)]) - 1


with open(input_1, mode="r") as text_file:
    rocks_instr = [[list(map(int, xy.split(","))) for xy in line.split(" -> ")] for line in text_file.read().splitlines()]


rocks = np.empty(shape=[0, 2], dtype=int)
for line in rocks_instr:
    for num, pos in enumerate(line[:-1]):
        if line[num][0] == line[num + 1][0]:
            ys = (np.arange(sorted([line[num][1], line[num + 1][1]])[0],
                            sorted([line[num][1], line[num + 1][1]])[1] + 1))
            xs = np.full(ys.shape, fill_value=line[num][0])
            line_shape = np.vstack((xs, ys)).T
            rocks = np.vstack((rocks, line_shape))
        else:
            xs = (np.arange(sorted([line[num][0], line[num + 1][0]])[0],
                            sorted([line[num][0], line[num + 1][0]])[1] + 1))
            ys = np.full(xs.shape, fill_value=line[num][1])
            line_shape = np.vstack((xs, ys)).T
            rocks = np.vstack((rocks, line_shape))
rocks = np.unique(rocks, axis=0)
rocks = [tuple(rock) for rock in rocks]


sands = []
taken = rocks.copy()
x_start = 500
x_min = min([pos[0] for pos in rocks])
x_max = max([pos[0] for pos in rocks])
y_max_depth = max([pos[1] for pos in rocks])
y_min_depth = min([pos[1] for pos in rocks])


x = x_start
y_limit = 0
for _ in range(1):
    y_fall = good_y(x, y_limit, taken)
    x_left, x_right = x - 1, x + 1
    y_left, y_right = good_y(x_left, y_fall, taken), good_y(x_right, y_fall, taken)
    print(y_fall, y_left, y_right)
    x_left_try, x_right_try = x_left - 1, x_right + 1
    y_left_try, y_right_try = good_y(x_left_try, y_left, taken), good_y(x_right_try, y_right, taken)
    while y_left > y_fall and y_right > y_fall:
        print("left")
        while tuple([x_left_try, y_left_try]) not in taken and x_left_try > x_min:
            x_left_try = x_left - 1
            y_left_try = good_y(x_left_try, y_fall, taken)
        sands.append(tuple([x_left, y_left]))
        taken.append(tuple([x_left, y_left]))
    #     while tuple([x_right_try, y_right_try]) not in taken and x_right_try < x_max:
    #         x_right_try = x_right + 1
    #         y_right_try = good_y(x_right_try, y_fall, taken)
    #     sands.append(tuple([x_right, y_right]))
    #     taken.append(tuple([x_right, y_right]))
    # sands.append(tuple([x, y_fall]))
    # taken.append(tuple([x, y_fall]))
    # y_fall = good_y(x, y_limit, taken)


sand_row = []
all_sands = []
rock_row = []
all_rocks = []
for row in range(y_max_depth + 1):
    sand_row = [int(tuple([col, row]) in sands) for col in range(x_min,  x_max + 1)]
    all_sands.append(sand_row)
    rock_row = [int(tuple([col, row]) in rocks) for col in range(x_min, x_max + 1)]
    all_rocks.append(rock_row)

all_sands = np.array(all_sands)
all_rocks = np.array(all_rocks) * 4
all_rs = all_sands + all_rocks

# print(all_sands)

plt.imshow(all_rs)
plt.show()


