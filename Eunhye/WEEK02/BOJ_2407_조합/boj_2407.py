import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = 1
divider = 1

for i in range(1, m+1):
  result *= n
  divider *= i
  n -= 1

print(result // divider)