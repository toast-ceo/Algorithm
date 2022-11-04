# Input
data1 = ['5', '4 1 5 2 3', '5', '1 3 7 9 5']

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

n = input()
N = sorted(map(int, input().split()))
m = input()
M = map(int, input().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l, N, start, end))