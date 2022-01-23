from typing import TypeVar, Generic, List, Callable
import re
from queue import Queue


class Operator:
    # representation: str
    # precedence: int
    # leftAssociative: bool
    # operation: Callable
    def __init__(self, representation, precedence, leftAssociative, operation):
        self.representation = representation
        self.precedence = precedence
        self.leftAssociative = leftAssociative
        self.operation = operation

    def calculate(self, operand1, operand2):
        return self.operation(operand1, operand2)

    def __repr__(self):
        return self.representation


class Stack:
    # container: List[T]
    def __init__(self):
        self.container = []

    def empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def top(self):
        return self.container[-1]

    def push(self, element):
        self.container.append(element)

    def pop(self):
        return self.container.pop()


def eval(queue: Queue):
    stack = Stack()
    while not queue.empty():
        element = queue.get()
        if type(element) is int:
            stack.push(element)
        else:  # operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = element.calculate(operand1, operand2)
            stack.push(result)
    return stack.pop()


def isNumber(token):
    return bool(re.match(r'\d+', token))


def infixToRPN(input: str):
    input = input.replace('(', '( ')
    input = input.replace(')', ' )')
    input = input.strip()
    tokens = input.split(' ')
    output_queue = Queue()
    operator_stack = Stack()
    operators = {
        '+': Operator('+', 2, True, lambda l, r: l+r),
        '*': Operator('*', 1, True, lambda l, r: l*r)
    }
    for token in tokens:
        if isNumber(token):
            output_queue.put(int(token))
        elif operator := operators.get(token):
            while (not operator_stack.empty()
                   and operator_stack.top() != '('
                   and (operator_stack.top().precedence > operator.precedence
                        or (operator_stack.top().precedence == operator.precedence
                            and operator.leftAssociative))):
                output_queue.put(operator_stack.pop())
            operator_stack.push(operator)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            while not operator_stack.top() == '(':
                output_queue.put(operator_stack.pop())
            if operator_stack.top() == '(':
                operator_stack.pop()
    while not operator_stack.empty():
        output_queue.put(operator_stack.pop())
    return output_queue

if __name__ == '__main__':
    f = open('input.txt', 'r')
    lines = f.readlines()
    result = 0
    for line in lines:
        rpn = infixToRPN(line)
        result += eval(rpn)
    print(result)
