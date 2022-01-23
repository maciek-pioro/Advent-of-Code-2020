import re

def deconstruct(line):
    regex = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'
    parts = re.match(regex, line)
    return parts.group(1), parts.group(2), parts.group(3), parts.group(4)

f = open('input.txt', 'r')

validPasswords = 0
for l in f:
    m, M, l, s = deconstruct(l)
    if int(m) <= s.count(l) <= int(M):
        validPasswords += 1
print(validPasswords)