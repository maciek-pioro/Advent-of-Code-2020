f = open('input.txt', 'r')
# f = open('example2.txt', 'r')

def countPaths(graph: dict[int, list[int]], begin: int, available_paths: list[int]) -> int:
    if available_paths[begin] > -1:
        return available_paths[begin]
    result = 0
    for neighbor in graph[begin]:
        result += countPaths(graph, neighbor, available_paths)
    available_paths[begin] = result
    return result

adapters_sorted = [0] + sorted([int(l) for l in f])
max_adapter = adapters_sorted[-1]
available_adapters = (max_adapter + 4) * [False]
available_paths = (max_adapter + 4) * [-1]
available_paths[max_adapter] = 1
graph: dict = dict()

for adapter in adapters_sorted[::-1]:
    available_adapters[adapter] = True
    for i in [1, 2, 3]:
        if available_adapters[adapter + i]:
            if graph.get(adapter) is None:
                graph[adapter] = []
            graph[adapter] += [adapter + i]

print(countPaths(graph, 0, available_paths))