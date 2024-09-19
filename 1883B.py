for _ in range(int(input())):
    _, k = map(int, input().split())
    s = input()
    parity = [0] * 26
    for c in s:
        parity[ord(c) - 97] ^= 1
    print("YES" if sum(parity) - k <= 1 else "NO")
