import re
import numpy as np
from copy import deepcopy


# input_1 = "input_11.txt"
input_1 = "test_input.txt"


class Monkeys:

    all_items = np.array([], dtype="q")
    initial_items = np.array([], dtype="q")
    reduce = 1
    item_id = 0

    def __init__(self, init_orders):
        self.init_orders = init_orders
        self.held_items_indexes = np.array([], dtype="i")
        self.operation = None
        self.test = None
        self.throw_to_true_false = None, None
        self.handle_init_orders()
        self.inspection_count = 0

    def handle_init_orders(self):
        for item in (int(num) for num in re.findall(r"\d+", self.init_orders[1])):
            Monkeys.all_items = np.append(Monkeys.all_items, item)
            Monkeys.initial_items = np.append(Monkeys.initial_items, item)
            self.held_items_indexes = np.append(self.held_items_indexes, Monkeys.item_id)
            Monkeys.item_id += 1
        self.throw_to_true_false = int(self.init_orders[4].split()[-1]), int(self.init_orders[5].split()[-1])
        self.test = np.vectorize(lambda x: x % int(self.init_orders[3].split()[-1]) == 0, otypes="?")
        Monkeys.reduce = Monkeys.reduce * int(self.init_orders[3].split()[-1])

        if self.init_orders[2].split()[-1].isdigit() and self.init_orders[2].split()[-2] == "+":
            self.operation = np.vectorize(lambda x: x + int(self.init_orders[2].split()[-1]), otypes="q")
        if self.init_orders[2].split()[-1].isdigit() and self.init_orders[2].split()[-2] == "*":
            self.operation = np.vectorize(lambda x: x * int(self.init_orders[2].split()[-1]), otypes="q")
        if (not self.init_orders[2].split()[-1].isdigit()) and self.init_orders[2].split()[-2] == "+":
            self.operation = np.vectorize(lambda x: x + x, otypes="q")
        if (not self.init_orders[2].split()[-1].isdigit()) and self.init_orders[2].split()[-2] == "*":
            self.operation = np.vectorize(lambda x: x ** 2, otypes="q")

    def one_monkey_operation(self, monkey_list, worry_relief=False):
        self.inspection_count += self.held_items_indexes.size

        Monkeys.all_items[self.held_items_indexes] = self.operation(Monkeys.all_items[self.held_items_indexes])
        Monkeys.all_items[self.held_items_indexes] = Monkeys.all_items[self.held_items_indexes] % Monkeys.reduce

        if worry_relief:
            Monkeys.all_items[self.held_items_indexes] = Monkeys.all_items[self.held_items_indexes] // 3

        tested_indexes = self.test(Monkeys.all_items[self.held_items_indexes])
        monkey_list[self.throw_to_true_false[0]].held_items_indexes = np.append(
            monkey_list[self.throw_to_true_false[0]].held_items_indexes, self.held_items_indexes[tested_indexes])
        monkey_list[self.throw_to_true_false[1]].held_items_indexes = np.append(
            monkey_list[self.throw_to_true_false[1]].held_items_indexes, self.held_items_indexes[~tested_indexes])
        self.held_items_indexes = np.array([], dtype="i")

    @classmethod
    def reset_worry(cls):
        cls.all_items = np.copy(cls.initial_items)


m = []
monkeys = []

with open(input_1, mode="r") as text_file:
    while True:
        line = text_file.readline()
        if not line:
            break
        if line == "\n":
            monkeys.append(Monkeys(m))
            m = []
        else:
            m.append(line.strip())
    monkeys.append(Monkeys(m))

monkeys2 = deepcopy(monkeys)

# # TASK 1
for _ in range(20):
    for mo in monkeys:
        mo.one_monkey_operation(monkeys, worry_relief=True)

inspections = sorted([mo.inspection_count for mo in monkeys], reverse=True)
print(inspections[0] * inspections[1])  # for test input 76728

Monkeys.reset_worry()

# # TASK 2
for _ in range(10000):
    for mo2 in monkeys2:
        mo2.one_monkey_operation(monkeys2)

inspections2 = sorted([mo2.inspection_count for mo2 in monkeys2], reverse=True)
print(inspections2[0] * inspections2[1])   # for test input 2713310158
