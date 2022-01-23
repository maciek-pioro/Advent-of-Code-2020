DIGITS = [str(i) for i in range(0, 10)]

class Operator:
    def __init__(self, representation: str, operation, precedence: int, rightAssociative: bool=False):
        self.representation = representation
        self.operation = operation
        self.precedence = precedence
        self.rightAssociative = rightAssociative

class ExpressionText:
    def __init__(self, text: str, operators: list[str]):
        self.text = text.replace(' ', '').replace('\t', '').replace('\n', '')
    def tokens(self):
        left = self.text
        while left != '':
            
        
    
operators = [
    Operator('+', lambda l, r: l+r, 1, False),
    Operator('*', lambda l, r: l*r, 1, False)
]

input = '2+3'

buf = ''
output_queue = []
operator_stack = []
for c in input:
    if c in DIGITS:
        buf += c
        continue
    