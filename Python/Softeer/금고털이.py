from sys import stdin

input = stdin.readline

W, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[1], reverse=True)

result = 0
for m, p in arr:
    if W - m >= 0:
        W -= m
        result += (m * p)
        # 크기만큼 안될때에 잘라야하는 부분
    else:
        result += (W * p)
        break

print(result)