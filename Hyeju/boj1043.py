# 거짓말
import sys

N, M = map(int, sys.stdin.readline().split())
truth = set(list(map(int, sys.stdin.readline().split()))[1:])
party = []

for i in range(M):
    party.append(list(map(int, sys.stdin.readline().split()))[1:])

def solve():
    flag = 0
    for i in range(M):
        for j in range(len(party[i])):
            if party[i][j] in truth:
                tmp = len(truth)
                truth.update(party[i])
                if tmp < len(truth):
                    flag = 1
                break
    return flag

tmp = 1
while tmp:
    tmp = solve()

ans = 0
for i in range(M):
    flag = 1
    for j in range(len(party[i])):
        if party[i][j] in truth:
            flag = 0
            break
    if flag:
        ans += 1
print(ans)