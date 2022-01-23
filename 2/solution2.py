import re

def deconstruct(line):
    regex = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'
    parts = re.match(regex, line)
    return parts.group(1), parts.group(2), parts.group(3), parts.group(4)

f = open('input.txt', 'r')

validPasswords = 0
for l in f:
    m, M, l, s = deconstruct(l)
    v1 = s[int(m)-1] == l
    v2 = s[int(M)-1] == l
    if v1 ^ v2:
        validPasswords += 1
print(validPasswords)