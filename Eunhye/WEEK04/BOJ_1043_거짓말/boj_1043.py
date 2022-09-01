import sys

input = sys.stdin.readline

N, M = map(int,input().split())
truth = set(list(map(int, input().split()))[1:])
result = M
parties = []

for _ in range(M):
  members = set(list(map(int, input().split()))[1:])
  parties.append(members)

for _ in range(M):
  for party in parties:
    if party & truth:
      truth = truth | party

for party in parties:
  if party & truth:
    result -= 1

print(result)