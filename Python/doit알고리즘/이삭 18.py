import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
temp = 0
for i in range(n):
    temp += arr[i]
    ans += temp
print(ans)