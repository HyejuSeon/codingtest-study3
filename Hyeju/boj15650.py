# N과 M (2)
import sys
N, M = map(int, sys.stdin.readline().split())
A = []
def dfs(s):
    if len(A) == M:
        print(" ".join(A))
        return

    for i in range(s, N + 1):
        A.append(str(i))
        dfs(i + 1)
        A.pop()

dfs(1)