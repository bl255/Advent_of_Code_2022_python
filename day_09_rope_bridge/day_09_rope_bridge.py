input_1 = "input_09.txt"
# input_1 = "test_input.txt"


def move(position, lrup, amount=1):
    if lrup == "R":
        position[0] += amount
    elif lrup == "L":
        position[0] -= amount
    elif lrup == "U":
        position[1] += amount
    elif lrup == "D":
        position[1] -= amount
    else:
        raise ValueError
    return position


class RopeState:

    def __init__(self):
        self.beginning = (0, 0)
        self.head_pos = list(self.beginning)
        self.tail_pos = list(self.beginning)
        self.tail_visited = []
        self.tail_visited.append(tuple(self.beginning))

    def update_head(self, head_move):
        direct = head_move.split()[0]
        self.head_pos = move(self.head_pos, direct)

    def update_tail(self):
        # proximity = self.tail_proximity()
        if self.tail_pos not in self.head_proximity():
            self.tail_pos = self.tail_proximity()[self.tail_follow_index()]
            self.tail_visited.append(tuple(self.tail_pos))

    def tail_follow_index(self):
        orient = ""
        orient_index = {"ul": 0, "u": 1, "ur": 2,
                        "l": 3, "c": 4, "r": 5,
                        "dl": 6, "d": 7, "dr": 8}
        if self.tail_pos[1] < self.head_pos[1]:
            orient = orient + "u"
        if self.tail_pos[1] > self.head_pos[1]:
            orient = orient + "d"
        if self.tail_pos[0] < self.head_pos[0]:
            orient = orient + "r"
        if self.tail_pos[0] > self.head_pos[0]:
            orient = orient + "l"
        if self.tail_pos == self.head_pos:
            orient = "c"
        return orient_index[orient]

    def update_rope(self, rope_move):
        move_interval = int(rope_move.split()[1])
        for one in range(move_interval):
            self.update_head(rope_move)
            print(self.head_pos, self.tail_follow_index(), self.tail_proximity()[self.tail_follow_index()])
            self.update_tail()
            print(self.head_pos, self.tail_pos)

    def tail_proximity(self):
        x, y = self.tail_pos
        return [[x - 1, y + 1], [x, y + 1], [x + 1, y + 1],
                [x - 1, y], [x, y], [x + 1, y],
                [x - 1, y - 1], [x, y - 1], [x + 1, y - 1]]

    def head_proximity(self):
        x, y = self.head_pos
        return [[x - 1, y + 1], [x, y + 1], [x + 1, y + 1],
                [x - 1, y], [x, y], [x + 1, y],
                [x - 1, y - 1], [x, y - 1], [x + 1, y - 1]]


with open(input_1, mode="r") as text_file:
    rope_moves = [line for line in text_file.read().splitlines()]


rope1 = RopeState()


for i_move in rope_moves:
    rope1.update_rope(i_move)
    # rope1.update_head(i_move)
    # rope1.update_tail()
    # print()
    # print(rope1.head_pos)
    # print(rope1.head_pos)
    # print(rope1.head_proximity())
    # print()
print(len(set(rope1.tail_visited)))
# print(rope1.head_pos)
# print(rope1.head_proximity())

