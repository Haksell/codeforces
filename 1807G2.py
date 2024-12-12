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
        read()
        s, *a = sorted(mir())
        if s != 1:
            print("NO")
            continue
        for x in a:
            if x > s:
                print("NO")
                break
            s += x
        else:
            print("YES")


if __name__ == "__main__":
    main()
