import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))
s_arr = sorted(arr)
ans = []

for i in range(n):
    ans.append(s_arr[i][1] - arr[i][1])

print(max(ans)+1)