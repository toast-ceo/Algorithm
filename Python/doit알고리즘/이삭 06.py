import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(1, n + 1):
    if i ** 2 + i <= 2 * n and (2 * n - i ** 2 + i) % (2 * i) == 0:
        cnt += 1
print(cnt)