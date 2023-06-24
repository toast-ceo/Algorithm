from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

graph = [1 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1

    if arr[a] > arr[b]:
        graph[b] = 0
        continue
    elif arr[a] < arr[b]:
        graph[a] = 0
        continue
    else:
        graph[a] = 0
        graph[b] = 0
        continue

cnt = 0
for i in range(n):
    if graph[i] == 1:
        cnt += 1

print(cnt)