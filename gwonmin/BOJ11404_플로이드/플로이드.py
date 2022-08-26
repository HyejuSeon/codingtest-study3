import sys

# Inf의 범위가 작으면 틀릴 수 있으니 주의!!
Inf = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

#인접행렬 생성
d = [[Inf] * n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if d[a - 1][b - 1] > c:
        d[a - 1][b - 1] = c

#플로이드 와샬 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            # 자기 자신으로 오는 경우
            if j == i:
                d[i][j] = 0

            # k를 거쳐서 가는 값과 원래 값 중 최소 값
            else:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


for i in range(n):
    for j in range(n):
        if d[i][j] == Inf:
            print(0, end=' ')
        else:
            print(d[i][j], end=' ')
    print()
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

#인접 행렬
w = [[1e9]*n for _ in range(n)]

#자기 자신으로 가는 경우 0으로 초기화
for i in range(n):
    for j in range(n):
        if i == j:
            w[i][j] = 0

for _ in range(m):
    row, col, cost = map(int,input().split())
    w[row-1][col-1] = min(cost,w[row-1][col-1])

#플로이드 와샬 알고리즘
for i in range(n):
    for j in range(n):
        for k in range(n):
            w[j][k] = min(w[j][k],w[j][i]+w[i][k])

for row in w:
    for col in row:
        print(col, end = ' ')
    print()
'''