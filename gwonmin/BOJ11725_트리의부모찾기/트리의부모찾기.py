import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)

for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a] += [b]
    tree[b] += [a]

seq_lst = [0 for _ in range(n+1)]

def bfs(start):
    visited = set()
    visited.add(start)
    visit = deque()
    visit.append(start)

    while visit:
        par_node = visit.popleft()

        for child_node in tree[par_node]:
            if child_node not in visited:
                visited.add(child_node)
                visit.append(child_node)
                seq_lst[child_node] = par_node

bfs(1)
for par_node in seq_lst:
    if par_node != 0:
        print(par_node)

