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
        read()
        res = []
        a = []
        broken = False
        for x in mir():
            if not broken:
                if a and x < a[-1]:
                    if x <= a[0]:
                        broken = True
                        a.append(x)
                        res.append("1")
                    else:
                        res.append("0")
                else:
                    a.append(x)
                    res.append("1")
            else:
                if x >= a[-1] and x <= a[0]:
                    a.append(x)
                    res.append("1")
                else:
                    res.append("0")
        print("".join(res))


if __name__ == "__main__":
    main()