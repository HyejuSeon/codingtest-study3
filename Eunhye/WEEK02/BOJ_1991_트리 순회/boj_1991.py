import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
tree = dict()
for _ in range(N):
  parent, left, right = input().split()
  tree[parent] = (left, right)

pre = []
in_ = []
post = []

def preorder(node):
  left, right = tree[node]
  pre.append(node)
  if left != ".":
    preorder(left)
  if right != ".":
    preorder(right)


def inorder(node):
  left, right = tree[node]
  if left != ".":
    inorder(left)
  in_.append(node)
  if right != ".":
    inorder(right)


def postorder(node):
  left, right = tree[node]
  if left != ".":
    postorder(left)
  if right != ".":
    postorder(right)
  post.append(node)


preorder("A")
inorder("A")
postorder("A")
print(*pre, sep="")
print(*in_, sep="")
print(*post, sep="")