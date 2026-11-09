nodes, edges = map(int, input().split())
bribes = list(map(int, input().split()))
graph = [[] for _ in range(nodes)]
for _ in range(edges):
    u, v = (int(x) - 1 for x in input().split())
    graph[u].append(v)
    graph[v].append(u)

res = 0
seen = set()
for i in range(nodes):
    if i in seen:
        continue
    cheapest = bribes[i]
    component = {i}
    stack = [i]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in component:
                cheapest = min(cheapest, bribes[neighbor])
                component.add(neighbor)
                stack.append(neighbor)
    seen |= component
    res += cheapest
print(res)
