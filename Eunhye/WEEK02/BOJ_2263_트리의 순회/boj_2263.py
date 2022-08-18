import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())

pre = []
in_ = list(map(int, input().split()))
post = list(map(int, input().split()))

in_position = [0 for _ in range(N+1)]

for i, node in enumerate(in_):
  in_position[node] = i

def preorder(in_start, in_end, post_start, post_end):
  if (in_start > in_end) or (post_start > post_end):
        return
    
  root = post[post_end]
  
  left = in_position[root] - in_start
  right = in_end - in_position[root]
  
  pre.append(root)
  preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)
  preorder(in_end - right + 1, in_end, post_end - right, post_end - 1)

preorder(0, N-1, 0, N-1)
print(*pre, sep=" ")