# 메모리를 봐야함
# import sys를 하고 sys.stdin.readline()를 써야지 런타임 에러가 나지 않음
import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 10001

for i in range(N):
    temp = int(input())
    arr[temp] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)