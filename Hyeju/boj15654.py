# N과 M (5)
import sys
N, M = map(int, sys.stdin.readline().split())
A = sorted(list(map(int, sys.stdin.readline().split())))
ans = []
tmp = []

def dfs():
    if len(tmp) == M:
        ans.append(tmp.copy())
        return

    for i in range(N):
        n = str(A[i])
        if n not in tmp:
            tmp.append(n)
            dfs()
            tmp.pop()

dfs()
for a in ans:
    print(" ".join(a))