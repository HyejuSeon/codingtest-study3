# 루트없는 트리가 주어진다. 트리의 루트를 1이라고 지정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n=int(input())
tree=[[] for _ in range(n+1)]

for i in range(n-1):
    n1,n2=map(int,input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

visited=[0]*(n+1)

def dfs(s):
    for i in tree[s]:
        if visited[i]==0:
            visited[i]=s
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(visited[i])