# Input
data1 = ['10 4200', '1', '5', '10', '50', '100', '500', '1000', '5000', '10000', '50000']

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

n, target = map(int, input().split())
coins = []
answer = 0
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)


for coin in coins:
    answer += target // coin
    target = target % coin
print(answer)