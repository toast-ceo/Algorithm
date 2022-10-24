import sys
from collections import deque

input = sys.stdin.readline
dq = deque()

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    while dq and dq[-1][1] > arr[i]:
        dq.pop()
    dq.append((i, arr[i]))

    while dq and dq[0][0] < i - m + 1:
        dq.popleft()

    print(dq[0][1], end=' ')
