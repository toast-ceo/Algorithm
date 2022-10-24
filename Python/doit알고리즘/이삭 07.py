import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = sorted(list(map(int, input().split())))
cut = 0
L, R = 0, len(arr) - 1

while L != R:
    s = arr[L] + arr[R]
    if s == m:
        cut += 1
        R -= 1
    elif s < m:
        L += 1
    elif s > m:
        R -= 1
print(cut)