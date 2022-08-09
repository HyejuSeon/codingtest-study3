import sys

input = sys.stdin.readline

N = int(input())

costs = [list(map(int,input().split())) for _ in range(N)]

for c_idx in range(1,len(costs)):
    for i in range(3):
        if i == 0:
            costs[c_idx][i] = min(costs[c_idx][i] + costs[c_idx - 1][1], costs[c_idx][i] + costs[c_idx - 1][2])
        if i == 1:
            costs[c_idx][i] = min(costs[c_idx][i] + costs[c_idx - 1][0], costs[c_idx][i] + costs[c_idx - 1][2])
        if i == 2:
            costs[c_idx][i] = min(costs[c_idx][i] + costs[c_idx - 1][0], costs[c_idx][i] + costs[c_idx - 1][1])

print(min(costs[-1]))


