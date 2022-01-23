f = open('input.txt')

numbers = [int(l) for l in f]
PREAMBLE_LENGTH = 25
SUM = 167829540

prefix_sum = numbers[:]
for i in range(1, len(numbers)):
    prefix_sum[i] += prefix_sum[i-1]

for i in range(len(numbers)):
    for j in range(i + 2, len(numbers)):
        if prefix_sum[j] - prefix_sum[i] == SUM:
            m = min(numbers[i+1:j])
            M = max(numbers[i+1:j])
            print(m)
            print(M)
            print(m + M)
            exit()


