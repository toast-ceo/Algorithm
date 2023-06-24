"""
1.BFS
2.

graph --BFS-->time

"""

# C 표시 지우기
def eliminate():
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:
                graph[i][j] = 0
            elif graph[i][j] >= 2:
                graph[i][j] = 1
    return

def bfs(a,b):
    q = deque([(a,b)]) # x,y
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if not graph[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                else:
                    graph[nx][ny] += 1
    eliminate()
    return

def check():
    for i in range(N):
        if sum(graph[i]):
            return True
    return False


import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

time = 0
while check():
    bfs(0,0)
    time += 1
print(time)
