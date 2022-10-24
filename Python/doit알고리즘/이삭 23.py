import sys
input = sys.stdin.readline
# python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러가 발생. 이를 방지
sys.setrecursionlimit(10000)

# 노드 개수 / 엣지 개수
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 엣지 개수만큼 입력을 받음
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

count = 0
for i in range(1, n+1):
    # 방문하지 않은 노드를 탐색 -> 연결 요소 개수
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)