import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

for a in combinations([i for i in range(1,n+1)],m):
    for b in a:
        print(b,end=' ')

    print()
