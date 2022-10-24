import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
s = 0
cnt = 0

for i, t in enumerate(arr):
    L, R = 0, n - 1
    while L != R:
        s = arr[L] + arr[R]
        if s == t and L != i and R != i:
            cnt += 1
            break
        if s < t or L == i:
            L += 1
        elif s > t or R == i:
            R -= 1
print(cnt)