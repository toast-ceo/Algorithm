import sys
input = sys.stdin.readline

def solution(n, m):
    n = int(n)
    m = list(map(int, m.split()))

    result = [-1] * n
    stack = []

    for i in range(len(m)):
        # 스택에 값이 있는지, m[stack[-1]]를 m[i]과 비교 (오 큰수 비교)
        while stack and m[stack[-1]] < m[i]:
            result[stack.pop()] = m[i]
        stack.append(i)

    print(*result)

num = input()
arg = input()
solution(num, arg)