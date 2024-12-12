# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n, q = mir()
        a = lmir()
        xs = []
        for i in range(20):
            x0 = [0]
            x1 = [0]
            for ai in a:
                if ai & (1 << i):
                    x0.append(x0[-1])
                    x1.append(x1[-1] ^ ai)
                else:
                    x0.append(x0[-1] ^ ai)
                    x1.append(x1[-1])
            xs.append(x0)
            xs.append(x1)
        for _ in range(q):
            l, r = mir()
            count = r - l + 1
            print(
                "YES" if count & 1 == 0 and all(x[r] == x[l - 1] for x in xs) else "NO"
            )


if __name__ == "__main__":
    main()
