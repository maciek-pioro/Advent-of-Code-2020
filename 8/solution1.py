import re

f = open('input.txt', 'r')

program = f.readlines()

accumulator = 0
instruction_counter = 0
instructions_length = len(program)
executed_instructions = instructions_length * [False]

while(instruction_counter < instructions_length):
    if executed_instructions[instruction_counter]:
        break
    executed_instructions[instruction_counter] = True
    current_instruction = program[instruction_counter]
    match = re.search(r'([a-z]+) ((\+|-)(\d+))', current_instruction)
    instruction = match.group(1)
    argument = int(match.group(2))
    if instruction == 'acc':
        accumulator += argument
        instruction_counter += 1
    elif instruction == 'nop':
        instruction_counter += 1
    elif instruction == 'jmp':
        instruction_counter += argument

print(accumulator)

