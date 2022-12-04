import re
import numpy as np

input_1 = "input_04.txt"
# input_1 = "test_input.txt"

with open(input_1, mode="r") as text_file:
    sectors = (tuple(map(int, re.split(r"[-,]", line))) for line in text_file.read().splitlines())

sector_arrs = [tuple([np.arange(sector[0], sector[1] + 1), np.arange(sector[2], sector[3] + 1)]) for sector in sectors]

# TASK 1
all_contained = sum((all(np.isin(arr[0], arr[1])) or all(np.isin(arr[1], arr[0])) for arr in sector_arrs))
print(all_contained)  # for me 651

# TASK 2
all_overlaping = sum((np.intersect1d(arr[0], arr[1]).shape[0] > 0 for arr in sector_arrs))
print(all_overlaping)  # for me 956
