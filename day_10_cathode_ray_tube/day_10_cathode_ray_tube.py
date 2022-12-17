import numpy as np
import matplotlib.pyplot as plt

# input_1 = "input_10.txt"
input_1 = "test_input.txt"

with open(input_1, mode="r") as text_file:
    signal = (line for line in text_file.read().splitlines())

cycle = 1
state_sum = 1
states = [1]
# sums_at_cycle = [(0, 1)]

for line in signal:
    # sums_at_cycle.append((cycle, state_sum))
    states.append(state_sum)
    cycle += 1
    if line[0] == "a":
        # sums_at_cycle.append((cycle, state_sum))
        states.append(state_sum)
        cycle += 1
        state_sum += int(line.split()[1])

print(sum(states[position] * position for position in (20, 60, 100, 140, 180, 220)))  # task1, test input 13140

# CONTINUING WITH TASK 2
row_pos = 0
row = []
screen = []

for c in range(1, 241):
    symbol = 0
    sub_sprite = states[c] + 1, states[c], states[c] - 1
    if row_pos in sub_sprite:
        symbol = 1
    row.append(symbol)
    if row_pos == 39:
        screen.append(row)
        row = []
        row_pos = 0
    else:
        row_pos += 1

# SIMPLE PLOT (set symbols to " " and █, or ♥ and ♠):
# for rw in screen:
#     print("".join(rw))

# PRETTIER PLOT WITH MATPLOTLIB
for_print = np.array(screen)
img = plt.imshow(for_print, cmap="Greys")
ax = plt.gca()
plt.axis("off")

plt.show()  # task 2

test_output = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
