# 연산자의 우선순위
'''
def prec(n):
    if (n == '(' or n == ')'):
        return 0
    elif (n == '+' or n == '-'):
        return 1
    elif (n == '*' or n == '/'):
        return 2

# 식 입력
calculation = input()

stack = []

for i in calculation:
    if (i.isalnum()):
        print(i, end='')
    else:
        if (i == '+' or i == '-' or i == '*' or i == '/'):
            # 우선순위가 늪은 것이 스택 밑에 있다면 낮은거 있을 때까지 pop()
            while (stack != [] and prec(i) <= prec(stack[-1])):
                print(stack.pop(), end='')
            stack.append(i)

        elif (i == '('):
            stack.append(i)

        elif (i == ')'):
            k = stack.pop()
            while (k != '('):
                print(k, end='')
                k = stack.pop()

while (stack != []):
    print(stack.pop(), end='')

'''

#연산자의 우선순위
def pri(oper):
    if oper == '(' or oper == ')':
        return 0
    if oper == '+' or oper == '-':
        return 1
    if oper == '*' or oper == '/':
        return 2

line = input()

stack = []

result = ''

for l in line:
    if l.isalpha():
        result += l

    else:
        if (l == '+' or l == '-' or l == '*' or l == '/'):
            while (len(stack) != 0 and pri(l) <= pri(stack[-1])):
                result += stack.pop()

            stack.append(l)

        elif (l == '('):
            stack.append(l)

        elif (l == ')'):
            temp = stack.pop()
            while temp != '(':
                result += temp
                temp = stack.pop()

while (stack != []):
    result += stack.pop()

print(result)






