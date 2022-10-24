import sys
# 덱을 이용해 시간초과 극복
from collections import deque
input = sys.stdin.readline

def solution(n):
    n = int(n)
    queue = deque()

    for i in range(n):
        queue.append(i+1)
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    print(queue.pop())

num = input()
solution(num)
