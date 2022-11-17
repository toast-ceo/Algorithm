# Input
data1 = ['100-40+50+74-30+29-45+43+11']

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

arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)

