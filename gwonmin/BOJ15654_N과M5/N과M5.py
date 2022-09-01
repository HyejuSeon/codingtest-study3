import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int,input().split())

n_lst = list(map(int,input().split()))
n_lst.sort()

for c in permutations(n_lst,m):
    for n in c:
        print(n,end=' ')
    print()

