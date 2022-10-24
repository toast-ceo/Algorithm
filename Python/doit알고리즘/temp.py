# Input
data1 = ['4 6', '101111', '101010', '101011', '111011']

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
