# Input
data1 = ['4 4 2 1', '1 2', '1 3', '2 3', '2 4']
data2 = ['4 3 2 1', '1 2', '1 3', '1 4']

def data():
    yield from data1

gen = data()

def readline():
    return next(gen)

from sys import stdin
stdin.readline = readline

# ----------
# Answer
import sys
from collections import deque
input = sys.stdin.readline

# N 도시 수, M 도로 수, K 거리 정보 X 출발 도시
N, M, K, X = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b =  map(int, input().split(' '))
  graph[a].append(b)

distance = [-1] *(N+1)
distance[X] = 0

# BFS 부분
q = deque([X])
while q:
  now = q.popleft()

  for next in graph[now]:
    if distance[next] == -1:
      distance[next] = distance[now]+1
      q.append(next)

# K값이 distance에 있다면 i값출력 없다면 -1 출력
if K in distance:
  for i in range(1, N+1):
    if distance[i] == K:
      print(i)
      check = True
else:
  print(-1)
