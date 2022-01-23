f = open('input.txt')

numbers : list[int] = [int(l) for l in f]
PREAMBLE_LENGTH = 25
SUM = 167829540

for i in range(len(numbers)):
    for j in range(i + 2, len(numbers)):
        if sum(numbers[i:j]) == SUM:
            print(min(numbers[i:j]))
            print(max(numbers[i:j]))
            print(min(numbers[i:j]) + max(numbers[i:j]))



