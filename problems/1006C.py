# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    a = lmir()
    lo = 0
    hi = n - 1
    res = sum1 = sum3 = 0
    while lo <= hi:
        if sum1 < sum3:
            sum1 += a[lo]
            lo += 1
        else:
            sum3 += a[hi]
            hi -= 1
        if sum1 == sum3:
            res = sum1
    print(res)


if __name__ == "__main__":
    main()
