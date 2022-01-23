f = open('input.txt')

numbers = [int(l) for l in f]
PREAMBLE_LENGTH = 25

for i in range(PREAMBLE_LENGTH, len(numbers)):
    canBeDone = False
    for j in range(i-PREAMBLE_LENGTH, i):
        for k in range(j, i):
            if numbers[j] + numbers[k] == numbers[i]:
                canBeDone = True
                break
        if canBeDone:
            break
    if not canBeDone:
        print(numbers[i])
        break
