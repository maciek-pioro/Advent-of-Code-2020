import re

f = open('input.txt', 'r')

program = f.readlines()

instructions_length = len(program)
instructionToChange=0
while True:
    accumulator = 0
    instruction_counter = 0
    executed_instructions = instructions_length * [False]
    jpmnopCounter = 0
    while instruction_counter < instructions_length:
        if executed_instructions[instruction_counter]:
            break
        executed_instructions[instruction_counter] = True
        current_instruction = program[instruction_counter]
        match = re.search(r'([a-z]+) ((\+|-)(\d+))', current_instruction)
        instruction = match.group(1)
        argument = int(match.group(2))
        if instruction in ['jmp', 'nop']:
            if instructionToChange == jpmnopCounter:
                if instruction == 'jmp':
                    instruction = 'nop'
                else:
                    instruction ='jmp'
            jpmnopCounter += 1
        if instruction == 'acc':
            accumulator += argument
            instruction_counter += 1
        elif instruction == 'nop':
            instruction_counter += 1
        elif instruction == 'jmp':
            instruction_counter += argument
    else:
        break
    instructionToChange += 1

print(accumulator)

