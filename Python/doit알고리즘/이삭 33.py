# Input
data1 = ['3', '10', '20', '40']

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
# 힙을 이용
import heapq


n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

if len(arr) == 1:
    print(0)
else:
    answer = 0
    while len(arr) > 1:
        temp1 = heapq.heappop(arr)
        temp2 = heapq.heappop(arr)
        answer += temp1 + temp2
        heapq.heappush(arr, temp1 + temp2)
    print(answer)