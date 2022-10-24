import sys
input = sys.stdin.readline

n = int(input())
# 값 넣는 리스트
stack = []
# 연산자 담는 리스트
op = []
cnt = 1
flag = True

for i in range(n):
    temp = int(input())
    # 입력한 수를 만날 때까지 반복문을 돌림
    while cnt <= temp:
        stack.append(cnt)
        op.append("+")
        cnt += 1
    # 입력한 수를 만나면 while 문을 탈출, cnt == temp 일 때까지 스택을 쌓는 과정

    if stack[-1] == temp:
        stack.pop()
        op.append("-")
    else:
        print("NO")
        flag = False
        break

if flag:
    for i in op:
        print(i)