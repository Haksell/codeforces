# ruff: noqa: E731, E741
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, m = mir()
    f = randint(1, 1 << 30)

    graph = [[] for _ in range(n)]
    for _ in range(m):
        _, *friends = lmir()
        for f1, f2 in zip(friends, friends[1:]):
            graph[f1 - 1].append(f2 - 1)
            graph[f2 - 1].append(f1 - 1)

    components = [-1] * n
    for i in range(n):
        if components[i] != -1:
            continue
        stack = [i]
        component = {i + f}
        while stack:
            j = stack.pop()
            component.add(j + f)
            for k in graph[j]:
                if k + f not in component:
                    stack.append(k)
                    component.add(k + f)
        for c in component:
            components[c - f] = len(component)
    print(*components)


if __name__ == "__main__":
    main()
