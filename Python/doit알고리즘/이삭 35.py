# Input
data1 = ['11', '1 4', '3 5', '0 6', '5 7', '3 8', '5 9', '6 10', '8 11', '8 12', '2 13', '12 14']

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
room = []

for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])

room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])

answer = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        answer += 1
        end = room[i][1]

print(answer)