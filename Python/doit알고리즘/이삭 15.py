import sys
input = sys.stdin.readline

# 버블 정렬
def solution(n):
    n = int(n)
    arr = []
    for i in range(n):
        arr.append(int(input()))
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    for i in arr:
        print(i)
num = input()
solution(num)