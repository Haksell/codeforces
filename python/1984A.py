# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        if all(ai == a[0] for ai in a):
            print("NO")
            continue
        r = 0 if a[0] == a[1] else 2
        print("YES")
        print("".join("R" if i == r else "B" for i in range(n)))


if __name__ == "__main__":
    main()
