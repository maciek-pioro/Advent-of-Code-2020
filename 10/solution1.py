f = open('input.txt', 'r')
# f = open('example2.txt', 'r')


adapters_sorted = sorted([int(l) for l in f])

MAX_JOLTAGE_DIFF = 3

diffs = (MAX_JOLTAGE_DIFF + 1) * [0]

diffs[1] = 1
diffs[3] = 1

for i, adapter in enumerate(adapters_sorted[1:]):
    prev_adapter = adapters_sorted[i]
    diff = adapter - prev_adapter
    print(diff)
    diffs[diff] += 1

print(diffs)