def solve(c, s):
    c -= sum(si * si for si in s)
    n = len(s)
    t = sum(s)
    lo = 1
    hi = 1 << 30
    while True:
        mi = lo + hi >> 1
        margin = 4 * mi * (t + n * mi)
        if margin < c:
            lo = mi + 1
        elif margin > c:
            hi = mi - 1
        else:
            return mi


def main():
    for _ in range(int(input())):
        _, c = map(int, input().split())
        s = list(map(int, input().split()))
        print(solve(c, s))


if __name__ == "__main__":
    main()
