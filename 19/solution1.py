from typing import List


f = open('input1.txt', 'r')

class Rule:
    def __init__(self, content: str, depends_on: List[int]) -> None:
        self.content: str = content 
        self.depends_on: List[int] = depends_on
        self.possible_lengths: List[int] = []


lengths = [[] for i in range(200)]
for l in f:
    [rule_no, rule_content] = l.split(': ')
    if 'a' in rule_content or 'b' in rule_content:
        Rule
