# Input
data1 = ['4 5 1', '1 2', '1 3', '1 4', '2 4', '3 4']
data2 = ['5 5 3', '5 4', '5 2', '1 2', '3 4', '3 1']

def data():
    yield from data1

gen = data()

def readline():
    return next(gen)

from sys import stdin
stdin.readline = readline

# ----------

# Answer
from sys import stdin
input = stdin.readline

def dfs(v):
    # 현재 노드 방문 처리
    visited[v] = 1

    print(v, end=' ')

    # 현재 노드와 다른 노드를 재귀적으로 방문하는 부분
    for i in range(n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


# bfs 함수
def bfs(start):
    # 들려야 할 정점 저장
    queue = [start]

    # 현재 노드 방문 처리
    visited[start] = 0

    # 큐가 없을때까지 반복
    while queue:
        # 큐에서 하나의 원소를 팝하여 원소를 확인
        V = queue.pop(0)
        print(V, end=' ')

        # 아직 방문하지 않은 인접한 원소들을 큐에 추가
        for i in range(1, n + 1):
            if visited[i] == 1 and graph[V][i] == 1:
                queue.append(i)
                visited[i] = 0

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n + 1)

dfs(v)
print("")
bfs(v)