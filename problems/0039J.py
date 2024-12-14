# ruff: noqa: E731, E741
import sys

s1 = input()
s2 = input()
for i in range(len(s1)):
    if i == len(s2) or s1[i] != s2[i]:
        if s1[i + 1 :] != s2[i:]:
            break
        j = i - 1
        while j >= 0 and s1[j] == s1[i]:
            j -= 1
        print(i - j)
        print(*range(j + 2, i + 2))
        sys.exit()
print(0)
