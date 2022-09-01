import sys

input = sys.stdin.readline

n, m = map(int,input().split())

know_set = set(input().split()[1:])
parties = [set(input().split()[1:]) for _ in range(m)]

for _ in range(m):
    for party in parties:
        if party.intersection(know_set):
            know_set = know_set.union(party)

cnt = 0
for party in parties:
    if party.intersection(know_set):
        continue
    else:
        cnt += 1
print(cnt)