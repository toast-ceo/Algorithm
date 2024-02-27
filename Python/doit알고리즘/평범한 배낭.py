# Input
data1 = [
'4 7',
'6 13',
'4 8',
'3 6',
'5 12'
]

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

N,K = map(int,input().split())
items = []
for _ in range(N):
    w,v = map(int,input().split())
    items.append((w,v))
dp = [0 for _ in range(K+1)]
for item in items:
    w,v = item
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
print(dp[-1])