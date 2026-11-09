for _ in range(int(input())):
    _, r = map(int, input().split())
    print(r.bit_length() - 1)
