# ruff: noqa: E731, E741
for _ in range(int(input())):
    hp, void, lightning = map(int, input().split())
    for _ in range(void):
        if hp < 20:
            break
        hp >>= 1
        hp += 10
    hp -= 10 * lightning
    print("YES" if hp <= 0 else "NO")
