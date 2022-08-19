# 트리의 순회
import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

idx = [0] * (n + 1)
for i in range(n):
    idx[inorder[i]] = i

def preorder(in_l, in_r, post_l, post_r):
    if in_l > in_r or post_l > post_r:
        return
    root = postorder[post_r]
    print(root, end=" ")
    l = idx[root] - in_l
    r = in_r - idx[root]
    preorder(in_l, in_l + l - 1, post_l, post_l + l - 1)
    preorder(in_r - r + 1, in_r, post_r - r, post_r - 1)

preorder(0, n - 1, 0, n - 1)
