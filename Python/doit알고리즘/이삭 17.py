from sys import stdin
input = stdin.readline

# 선택 정렬
arr = list(map(int, input().strip()))

for i in range(len(arr)-1):
    min = i
    for j in range(i+1, len(arr)):
        if arr[min] < arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

# /n을 제거해줌
for i in arr:
    print(i, end="")