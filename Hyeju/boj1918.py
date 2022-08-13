#후위 표기식
from sys import stdin

def solve(op):
    global res
    if op == ')':
        while s[-1] != '(':
            res += s.pop()
        s.pop()
    else:
        while s:
            if s[-1] == '(' or ops[op] > ops[s[-1]]:
                break
            res += s.pop()
        s.append(op)

input = stdin.readline().strip()
res = ''
ops = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2, ')': 2}
s = []
for i in input:
    if i not in ops:
        res += i
    else:
        solve(i)
while s:
    res += s.pop()
print(res)