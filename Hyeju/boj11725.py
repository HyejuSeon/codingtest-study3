# 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
par = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(s):
    for i in tree[s]:
        if par[i] == 0:
            par[i] = s
            dfs(i)

dfs(1)

for i in range(2, N + 1):
    print(par[i])