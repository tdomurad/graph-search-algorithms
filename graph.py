def breadth_first_search(graph, starting_point):
    stack = [starting_point]
    visited = []
    edges = []
    while stack:
        if stack[0] not in visited:
            visited.append(stack[0])
        for each in graph[stack[0]]:
            if each not in visited and each not in stack:
                edges.append([stack[0], each])
                stack.append(each)
        stack.pop(0)

    print(f'BFS nodes: {visited}')

    print('BFS edges:')
    for edge in edges:
        print(f'\t{edge[0]} - {edge[1]}')


def depth_first_search(graph, starting_point):
    stack = [starting_point]
    visited = []
    edges = []
    while stack:
        if stack[-1] not in visited:
            visited.append(stack[-1])
        active = None
        temp = graph[stack[-1]]
        for each in reversed(temp):
            if each not in visited and each not in stack:
                active = each

        if active is not None:
            edges.append([stack[-1], active])
            stack.append(active)
        if active is None:
            stack.pop(-1)

    print(f'DFS nodes: {visited}')

    print('DFS edges:')
    for edge in edges:
        print(f'\t{edge[0]} - {edge[1]}')


file = open("input.txt", "r")

n = int(file.readline())
graph = {i: [] for i in range(n)}

i = 0
j = 0
for line in file:
    for number in line:
        if number == '1':
            graph[i].append(j)
        j += 1
    i += 1
    j = 0

print(graph)
breadth_first_search(graph, 0)
depth_first_search(graph, 0)
