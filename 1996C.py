for _ in range(int(input())):
    n, q = map(int, input().split())
    a = [ord(c) - 97 for c in input()]
    b = [ord(c) - 97 for c in input()]
    pca = [[0] * 26 for _ in range(n + 1)]
    pcb = [[0] * 26 for _ in range(n + 1)]
    for i, (ai, bi) in enumerate(zip(a, b)):
        for n in range(26):
            pca[i + 1][n] = pca[i][n] + (n == ai)
            pcb[i + 1][n] = pcb[i][n] + (n == bi)
    for _ in range(q):
        lo, hi = map(int, input().split())
        cnt_a = [pca[hi][n] - pca[lo - 1][n] for n in range(26)]
        cnt_b = [pcb[hi][n] - pcb[lo - 1][n] for n in range(26)]
        print(sum(abs(ai - bi) for ai, bi in zip(cnt_a, cnt_b)) >> 1)
