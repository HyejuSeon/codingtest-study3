# 숨바꼭질 3
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
A = [0] * 100001

q = deque()
q.append(N)
A[N] = 1
while q:
    curr = q.popleft()
    if curr == K:
       print(A[K] - 1)
       break
    for next in [2 * curr, curr - 1, curr + 1]:
        if 0 <= next < 100001 and not A[next]:
            if next == 2 * curr:
                A[next] = A[curr]
                q.appendleft(next)
            else:
                A[next] = A[curr] + 1
                q.append(next)