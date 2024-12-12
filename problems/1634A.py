# ruff: noqa: E731, E741
def is_palindrome(s):
    return all(s[i] == s[~i] for i in range(len(s) >> 1))


for _ in range(int(input())):
    _, k = map(int, input().split())
    s = input()
    print(2 - (k == 0 or is_palindrome(s)))
