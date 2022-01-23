import re

f = open('input.txt', 'r')
rules = []
sum_of_invalid_values = 0

for l in f.read().splitlines():
    if re.match(r'.*: (\d+)-(\d+).*', l):
        constraints: list[tuple[str, str]] = re.findall(r'(\d+)-(\d+)', l)
        parsed_constraints = [(int(m), int(M)) for (m, M) in constraints]
        rules += [parsed_constraints]
        print(constraints)
    elif re.match(r"(\d+,)*\d+", l):
        values = [int(n) for n in l.split(',')]
        passes = False
        for value in values:
            for rule in rules:
                for constraint in rule:
                    (m, M) = constraint
                    if m <= value <= M:
                        passes = True
                        break
        if passes:
            sum_of_invalid_values += value
print(sum_of_invalid_values)
