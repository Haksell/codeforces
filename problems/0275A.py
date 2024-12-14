# ruff: noqa: E731, E741
a, b, c = [int(x) & 1 for x in input().split()]
d, e, f = [int(x) & 1 for x in input().split()]
g, h, i = [int(x) & 1 for x in input().split()]
print(a ^ b ^ d ^ 1, a ^ b ^ c ^ e ^ 1, b ^ c ^ f ^ 1, sep="")
print(a ^ d ^ e ^ g ^ 1, b ^ d ^ e ^ f ^ h ^ 1, c ^ e ^ f ^ i ^ 1, sep="")
print(d ^ g ^ h ^ 1, e ^ g ^ h ^ i ^ 1, f ^ h ^ i ^ 1, sep="")
