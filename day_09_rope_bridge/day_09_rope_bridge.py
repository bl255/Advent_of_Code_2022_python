input_1 = "input_09.txt"
# input_1 = "test_input.txt"


def proximity(position):
    x, y = position
    return [[x - 1, y + 1], [x, y + 1], [x + 1, y + 1],
            [x - 1, y], [x, y], [x + 1, y],
            [x - 1, y - 1], [x, y - 1], [x + 1, y - 1]]


def follow_index(head_pos, tail_pos):
    orient = ""
    orient_index = {"ul": 0, "u": 1, "ur": 2,
                    "l": 3, "c": 4, "r": 5,
                    "dl": 6, "d": 7, "dr": 8}
    if tail_pos[1] < head_pos[1]:
        orient = orient + "u"
    if tail_pos[1] > head_pos[1]:
        orient = orient + "d"
    if tail_pos[0] < head_pos[0]:
        orient = orient + "r"
    if tail_pos[0] > head_pos[0]:
        orient = orient + "l"
    if tail_pos == head_pos:
        orient = "c"
    return orient_index[orient]


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

    def __init__(self, tail_len=1):
        self.beginning = (0, 0)
        self.tail_len = tail_len
        self.head_pos = list(self.beginning)
        self.body_pos_s = [list(self.beginning) for _ in range(self.tail_len)]
        self.tail_visited = set()
        self.tail_visited.add(self.beginning)

    def update_head(self, head_move):
        direct = head_move.split()[0]
        self.head_pos = move(self.head_pos, direct)

    def update_body(self):
        head_pos = self.head_pos
        for num, pos in enumerate(self.body_pos_s):
            if pos not in proximity(head_pos):
                pos = proximity(pos)[follow_index(head_pos, pos)]
                self.body_pos_s[num] = pos
                if num == self.tail_len - 1:
                    self.tail_visited.add(tuple(pos))
            head_pos = pos

    def update_rope(self, rope_move):
        move_interval = int(rope_move.split()[1])
        for one in range(move_interval):
            self.update_head(rope_move)
            self.update_body()


with open(input_1, mode="r") as text_file:
    rope_moves = (line for line in text_file.read().splitlines())

short_rope = RopeState(1)
long_rope = RopeState(9)

for i_move in rope_moves:
    short_rope.update_rope(i_move)
    long_rope.update_rope(i_move)

print(len(short_rope.tail_visited))  # task 1, for my input 5513
print(len(long_rope.tail_visited))  # task 2, for my input 2427
