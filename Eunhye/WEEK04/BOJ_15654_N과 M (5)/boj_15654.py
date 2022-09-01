from itertools import permutations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
seq = sorted(map(int, input().split()))
for combi in permutations(seq, M):
  print(*combi, sep=" ")