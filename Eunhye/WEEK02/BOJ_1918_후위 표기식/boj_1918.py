infix = input()
priority = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
postfix = []
stack = []

for ch in infix:
  if ord("A") <= ord(ch) <= ord("Z"):
    postfix.append(ch)
  else:
    if ch == "(": 
      stack.append(ch)
    elif ch == ")":
      while 1:
        popped = stack.pop()
        if popped == "(": 
          break
        postfix.append(popped)
    else:
      while stack and priority[ch] <= priority[stack[-1]]:
        postfix.append(stack.pop())
      stack.append(ch)
while stack:
  postfix.append(stack.pop())
print("".join(postfix))