from typing import Tuple, List
from functools import reduce

def normalizedCode(char):
    return ord(char) - ord('a')

f = open('input.txt')

section: str = ''
l: str
groups: List[str] = f.read().split('\n\n')
allChoices: List[Tuple[List[bool], int]] = []
for group in groups:
    choices = (normalizedCode('z') + 1) * [False]
    noOfChoices = 0
    for c in group:
        if (not 0 <= normalizedCode(c) <= normalizedCode('z')) or choices[normalizedCode(c)]:
            continue
        choices[normalizedCode(c)] = True
        noOfChoices += 1
    allChoices += [(choices, noOfChoices)]
print(reduce(lambda s, x: s + x[1], allChoices, 0))
