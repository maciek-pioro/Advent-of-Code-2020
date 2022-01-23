import re
from itertools import zip_longest


def combine_two_chars(v, m):
    if m == 'X':
        return v
    else:
        return m


def and_with_mask(value, mask):
    value_in_binary = format(value, '036b')
    value_in_binary = ''.join([combine_two_chars(v, m)
                                for v, m in zip(value_in_binary, mask)])
    return int(value_in_binary, 2)


f = open('input.txt', 'r')

lines = f.readlines()

instructions = []
memory = dict()
mask = 36*'X'
for line in lines:
    m = re.search(r'(mask) = (.*)|(mem)\[(.*)\] = (.*)', line)
    if m.group(1):  # mask
        mask = m.group(2)
    if m.group(3):  # mem
        address = int(m.group(4))
        value = int(m.group(5))
        memory[address] = and_with_mask(value, mask)
# print(memory.values())
print(sum(memory.values()))