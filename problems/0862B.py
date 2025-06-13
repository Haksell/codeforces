# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def handshake(n):
    return n * (n - 1) >> 1


def main():
    n = ir()
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mir()
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    seen = [False] * n
    even = odd = 0
    is_even = True
    level = [0]
    seen[0] = True
    while level:
        next_level = []
        for i in level:
            if is_even:
                even += 1
            else:
                odd += 1
            for j in tree[i]:
                if not seen[j]:
                    seen[j] = True
                    next_level.append(j)
        level = next_level
        is_even = not is_even
    print(odd * even - (n - 1))


if __name__ == "__main__":
    main()
