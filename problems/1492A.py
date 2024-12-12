# ruff: noqa: E731, E741
def next_meeting(numer, denom):
    return -(-numer // denom) * denom


for _ in range(int(input())):
    p, a, b, c = map(int, input().split())
    print(min(next_meeting(p, a), next_meeting(p, b), next_meeting(p, c)) - p)
