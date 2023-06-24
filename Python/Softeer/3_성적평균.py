from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(k):
    result = 0
    start, end = map(int, input().split())

    for i in range(start - 1, end):
        result += arr[i]
    print("%0.2f" % (result / (end - start + 1)))
