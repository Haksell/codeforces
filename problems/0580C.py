# ruff: noqa: E731, E741
size, maxi = map(int, input().split())
cats = list(map(int, input().split()))
tree = [[] for _ in range(size)]
for _ in range(size - 1):
    u, v = (int(n) - 1 for n in input().split())
    tree[u].append(v)
    tree[v].append(u)

result = 0
stack = [(0, cats[0])]
visited = set()
while stack:
    node, consecutive = stack.pop()
    if node != 0 and len(tree[node]) == 1:
        result += 1
        continue
    for child in tree[node]:
        if child in visited:
            continue
        if cats[child] and consecutive == maxi:
            continue
        stack.append((child, consecutive + 1 if cats[child] else 0))
        visited.add(child)
print(result)
