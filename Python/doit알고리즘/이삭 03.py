import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

temp = 0
result = [0] * (n + 1)

for i in range(n):
    temp += arr[i]
    result[i+1] = temp

for i in range(m):
    x, y = map(int, input().split())
    print(result[y] - result[x-1])