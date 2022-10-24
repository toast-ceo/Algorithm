from sys import stdin
input = stdin.readline


# 노드를 순서대로 방문하며 dfs를 수행
def dfs(idx, number):
    if number == 4:
        #존재할 경우 1출력 후 종료
        print(1)
        exit()
    for i in friend[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False


global visited, friend
N, M = map(int, input().split())
friend = [[] for _ in range(N)]
visited = [False] * N

# 그래프를 인접 리스트 방식으로 표현함
for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)


