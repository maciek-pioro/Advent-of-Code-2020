from typing import List, Tuple
import re


f = open('input.txt', 'r')


def extractRule(rule: str) -> Tuple[str, List[Tuple[int, str]]]:
    pattern: str = r'(?P<holder>.*) bags contain (?P<holdee>no other bags|.*)'
    match = re.search(pattern, rule)
    holder = match.group('holder')
    holdee = match.group('holdee')
    # print(holdee)
    if holdee == 'no other bags':
        return holder, []
    # Holder contains some other bags
    # holdeesPattern = r'((\d+ .*?)(?: bags?(?:, |\.)))+'
    holdeesPattern = r'\d+ .*?(?= bag)'
    holdees = re.findall(holdeesPattern, holdee)
    result = []
    for holdee in holdees:
        match = re.search(r'(?P<quantity>\d+) (?P<color>.*)', holdee)
        result += [(int(match.group(1)), match.group(2))]
        # print(result)
    # print(holder, result)
    return holder, result


def invertGraph(graph: dict) -> dict:
    res: dict = dict()
    for src, destinations in graph.items():
        if res.get(src) is None:
            res[src] = []
        for weight, destination in destinations:
            if res.get(destination) is None:
                res[destination] = []
            res[destination] += [(weight, src)]
    return res


def dfsCountReachable(graph: dict[str, List[Tuple[int, str]]], src: str) -> int:
    currentVertex: str = src
    res: int = 0
    seen = {vertex: False for vertex in graph.keys()}
    seen[src] = True
    stack: list[str] = [src]
    while len(stack) > 0:
        vertex: str = stack.pop()
        neighbors = graph[vertex]
        for _, neighbor in neighbors:
            if seen[neighbor]:
                continue
            seen[neighbor] = True
            res += 1
            stack.append(neighbor)
    return res


graph: dict = dict()
for l in f:
    holder, holdees = extractRule(l)
    graph[holder] = holdees
print(dfsCountReachable(invertGraph(graph), 'shiny gold'))