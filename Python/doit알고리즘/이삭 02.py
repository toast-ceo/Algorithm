import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = []

for i in arr:
    result.append(i / max(arr) * 100)
print(sum(result)/n)