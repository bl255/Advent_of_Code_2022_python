# input_1 = "input_13.txt"
input_1 = "test_input.txt"

# from collections import deque


with open(input_1, mode="r") as text_file:
    raw_signal = (line.strip("\n") for line in text_file.readlines())

signal_pairs = []
s = []

for item in raw_signal:
    if not item:
        signal_pairs.append(s)
        s = []
    else:
        s.append(item)
signal_pairs.append(s)


# for num, pair in enumerate(signal_pairs[:1], 1):
#     left, right = pair[0], pair[1]
#     while len(left) > 0 and len(right) > 0:
#         if all([left[0] == "[", left[-1] == "]", right[0] == "[", right[-1] == "]"]):
#             left, right = left[1:-1], right[1:-1]
#         if all()


