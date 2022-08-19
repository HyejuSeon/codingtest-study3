# 중위표기식 -> 후위표기식
exp=input()
stack=[]
answer=''

for i in exp:
    if i.isalpha():
        answer+=i
    else:
        if i=='(':
            stack.append(i)
        # +, - 발견 시 +,- 계산이 괄호에 포함된 것이 아니라면(=우선순위가 높지 않다면) 
        # 자신보다 우선순위가 높은 것들을 모두 문자열에 추가
        elif i=='+' or i=='-':
            while stack and stack[-1]!='(':
                answer+=stack.pop()
            stack.append(i)
        # *, / 발견 시 같은 우선순위에 있는 *, /를 모두 결과문자열에 추가 
        elif i=='*' or i=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                answer+=stack.pop()
            stack.append(i)
        # )를 발견하면 괄호 사이의 모든 연산자들을 결과문자열에 추가하고 (를 꺼내준다
        elif i==')':
            while stack and stack[-1]!='(':
                answer+=stack.pop()
            stack.pop()
    print(answer)

# 스택에 남아있는 모든 연산자를 결과문자열에 추가
while stack:
    answer+=stack.pop()

print(answer)
        
                

