# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = sorted(map(int, input().split()), reverse=True)
    alice = sum(x for x in a[::2] if x & 1 == 0)
    bob = sum(x for x in a[1::2] if x & 1 == 1)
    print("Alice" if alice > bob else "Bob" if bob > alice else "Tie")
