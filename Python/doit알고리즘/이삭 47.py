# Input
data1 = ['5 4', '3 1', '3 2', '4 3', '5 3']

def data():
    yield from data1

gen = data()

def readline():
    return next(gen)

from sys import stdin
stdin.readline = readline

# ----------
# Answer

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

array = [[] for _ in range(n+1)]

def bfs(v):
    q = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    cnt = 1
    while q:
        v = q.popleft()
        for node in array[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                cnt += 1

    return cnt

for _ in range(m):
    a, b = map(int, input().split())
    array[b].append(a)

results = []
max_value = -1
for i in range(1, n+1):
    result = bfs(i)
    if result > max_value:
        results = [i]
        max_value = result
    elif result == max_value:
        results.append(i)

for re in results:
    print(re, end=" ")