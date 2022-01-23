from typing import Tuple, List
from functools import reduce

def normalizedCode(char):
    return ord(char) - ord('a')

def logicalAnd(arrays: List[List[bool]]) -> List[bool]:
    res = arrays[0][:]
    for array in arrays:
        for i, val in enumerate(res):
            res[i] = val and array[i]
    return res

f = open('input.txt')

section: str = ''
l: str
groups: List[str] = f.read().split('\n\n')
allChoices: List[Tuple[List[bool], int]] = []
res = 0
for group in groups:
    persons = group.splitlines()
    groupChoices = (normalizedCode('z') + 1) * [True]
    for person in persons:
        personsChoices = (normalizedCode('z') + 1) * [False]
        for c in person:
            if (not 0 <= normalizedCode(c) <= normalizedCode('z')) or personsChoices[normalizedCode(c)]:
                continue
            personsChoices[normalizedCode(c)] = True
        groupChoices = logicalAnd([personsChoices, groupChoices])
    for choice in groupChoices:
        if choice:
            res += 1
print(res)