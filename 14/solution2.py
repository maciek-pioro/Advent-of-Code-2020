import re
from itertools import zip_longest


# def combine_two_chars_v1(v, m):
#     if m == 'X':
#         return v
#     else:
#         return m

# def combine_two_chars_v2(v, m):
#     if m in ['X', '1']:
#         return m
#     else:
#         return v

# def and_with_mask_v1(value, mask):
#     value_in_binary = format(value, '036b')
#     value_in_binary = ''.join([combine_two_chars_v1(v, m)
#                                 for v, m in zip(value_in_binary, mask)])
#     return int(value_in_binary, 2)

# def and_with_mask_v2(value, mask):
#     value_in_binary = format(value, '036b')
#     value_in_binary = ''.join([combine_two_chars(v, m)
#                                 for v, m in zip(value_in_binary, mask)])
#     return int(value_in_binary, 2)

def generate_addresses(mask: str, address: str) -> list[str]:
    result = ['']
    for i, (m, a) in enumerate(zip(mask, address)):
        if m == '0':
            result = [s + a for s in result]
        elif m=='1':
            result = [s + '1' for s in result]
        elif m=='X':
            result = [s + '0' for s in result] + [s + '1' for s in result]
    return result




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
        base_address = format(int(m.group(4)), '036b')
        value = int(m.group(5))
        for address in generate_addresses(mask, base_address):
            memory[address] = value
# print(memory.values())
print(memory)
print(sum(memory.values()))