input_1 = "input_06.txt"
# input_1 = "test_input.txt"

with open(input_1, mode="r") as text_file:
    whole_signal = text_file.read()


def first_unique_sequence(num_unq, signal=whole_signal):
    for num in range(len(signal) - (num_unq + 1)):
        if len(set(whole_signal[num: num + num_unq])) == num_unq:
            return num + num_unq


print(first_unique_sequence(4))  # for my input 1757
print(first_unique_sequence(14))  # for my input 2950
