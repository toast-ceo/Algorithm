from sys import stdin
input = stdin.readline

k, p ,n = map(int, input().split())
result = k

for _ in range(n):
    result = (result * p) % 1000000007

print(result )