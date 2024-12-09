# ruff: noqa: E731, E741
def pairs(s, left, right):
    ans = cnt = 0
    for c in s:
        if c == left:
            cnt += 1
        elif c == right and cnt > 0:
            cnt -= 1
            ans += 1
    return ans


def smart(s):
    return pairs(s, "(", ")") + pairs(s, "[", "]")


for _ in range(int(input())):
    print(smart(input()))
