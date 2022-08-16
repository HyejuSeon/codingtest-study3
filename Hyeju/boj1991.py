# 트리 순회
import sys
from collections import defaultdict

def preorder(n):
    if n == '.':
        return
    print(n, end="")
    preorder(tree[n][0])
    preorder(tree[n][1])

def inorder(n):
    if n == '.':
        return
    inorder(tree[n][0])
    print(n, end="")
    inorder(tree[n][1])

def postorder(n):
    if n == '.':
        return
    postorder(tree[n][0])
    postorder(tree[n][1])
    print(n, end="")

N = int(sys.stdin.readline())
tree = defaultdict(tuple)
for i in range(1, N + 1):
    p, l, r = map(str, sys.stdin.readline().split())
    tree[p] = l, r

preorder('A')
print()
inorder('A')
print()
postorder('A')