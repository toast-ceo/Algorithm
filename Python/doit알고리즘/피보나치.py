# Input
data1 = ['3', '0',
'1',
'3']

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

#피보나치
T = int(input())
for _ in range(T):
    N = int(input())
    zero,one=1,0 # zero: 0개수, one: 1개수
    for i in range(N):
        zero,one = one,zero+one # zero와 one에 대해 피보나치적용
    print(zero,one)