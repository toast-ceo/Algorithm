import sys

n, k = map(int, input().split())
arr = list(map(str, input()))

check = [False] * n

for i in range(n):

    if arr[i] == 'P':

        for j in range(i - k, i + k + 1):
            if j <= -1 or j >= n:
                continue
            if arr[j] == "H" and not check[j]:
                check[j] = True
                break

count = 0
for result in check:
    if result == True:
        count += 1

print(count)


