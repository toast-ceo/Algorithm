# Input
data1 = ['5', '1 3 2 -1', '2 4 4 -1', '3 1 2 4 3 -1', '4 2 4 3 3 5 6 -1', '5 4 6 -1']

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

n = int(input())
tree = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
maxDist = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    a = tmp[0]
    for i in range(1, len(tmp) - 1, 2):
        b, c = tmp[i], tmp[i + 1]
        tree[a].append((b, c))


def dfs(n, d):
    left, right = 0, 0
    for toNode, w in tree[n]:
        r = 0
        if not visit[toNode]:
            visit[toNode] = 1
            r = dfs(toNode, w)
        if left <= right:
            left = max(left, r)
        else:
            right = max(right, r)

    global maxDist
    maxDist = max(maxDist, left + right)
    return max(left + d, right + d)

visit[1] = 1
dfs(1, 0)
print(maxDist)