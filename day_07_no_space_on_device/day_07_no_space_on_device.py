input_1 = "input_07.txt"
# input_1 = "test_input.txt"


class Structure:

    def __init__(self):
        self.root = "/"
        self.current_position = self.root
        self.positions = []
        self.filenames = []
        self.filesizes = []

    def cd_all(self, input_line):
        cd_cmd = input_line[5:]
        if cd_cmd == "/":
            self.current_position = self.root
        elif cd_cmd == "..":
            self.current_position = (str(self.current_position).split("-", maxsplit=1)[1])
            if self.current_position not in self.positions:
                self.positions.append(self.current_position)
        else:
            self.current_position = "-".join((cd_cmd, str(self.current_position)))
            if self.current_position not in self.positions:
                self.positions.append(self.current_position)

    def handle_directory(self, input_line):
        dir_cmd = input_line[4:]
        new_pos = "-".join((dir_cmd, str(self.current_position)))
        if new_pos not in self.positions:
            self.positions.append(new_pos)

    def handle_file(self, input_line):
        val, f_name = input_line.split()
        val = int(val)
        whole_name = "-".join((f_name, self.current_position))
        if whole_name in self.filenames:
            file_id = self.filenames.index(whole_name)
            self.filesizes[file_id] = val
        else:
            self.filenames.append(whole_name)
            self.filesizes.append(val)

    def handle_ls(self, input_line):
        pass

    def long_input(self, long_input):
        for input_line in long_input:
            if input_line[:4] == "$ cd":
                self.cd_all(input_line)
            elif input_line[:4] == "$ ls":
                self.handle_ls(input_line)
            elif input_line[:3] == "dir":
                self.handle_directory(input_line)
            elif input_line[0].isdigit():
                self.handle_file(input_line)
            else:
                raise ValueError

    @property
    def sum_vals(self):
        s_dict = {dir_k: 0 for dir_k in self.positions}
        for num, fl in enumerate(self.filenames):
            fdr = fl.split("-", maxsplit=1)[1]
            val = self.filesizes[num]
            for k in s_dict:
                if k in fdr:
                    s_dict[k] = s_dict[k] + val
        return s_dict.values()


with open(input_1, mode="r") as text_file:
    whole_input = (line for line in text_file.read().splitlines())


my_device = Structure()
my_device.long_input(whole_input)


total_size = 70000000
need = 30000000
taken = max(my_device.sum_vals)
have_free = total_size - taken
need_to_add = need - have_free

print(sum([value for value in my_device.sum_vals if value <= 100000]))  # my input 1501149
print(min([val for val in my_device.sum_vals if val >= need_to_add]))  # my input 10096985

