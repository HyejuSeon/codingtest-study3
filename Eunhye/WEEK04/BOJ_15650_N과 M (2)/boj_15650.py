from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
for combi in combinations(range(1, N+1), M):
  print(*combi, sep=" ")