# Input
data1 = ['9 3', '1 2 3 4 5 6 7 8 9']

def data():
    yield from data1

gen = data()

def readline():
    return next(gen)

from sys import stdin
stdin.readline = readline

# ----------
# Answer
from sys import stdin
input = stdin.readline

n, m = map(int,input().split())
data = list(map(int,input().split()))

num = sum(data)

start = 0
end = 10000000000
result = num

while start <= end:

    # mid 는 블루레이 크기
    mid = (start+end) // 2
    if mid < max(data):
        start = mid + 1
        continue

    # cnt 는 블루레이 개수 , tmp 는 블루레이 갱신해주고 있는 블루레이 길이
    cnt, tmp = 1, 0

    # 하나씩 더하면서 갱신해준다.
    for i in range(len(data)):
        # 이전 값이랑 지금 값 더해서 mid 보다 작으면 계속 더해준다
        if tmp + data[i] <= mid:
            tmp += data[i]
        # mid 보다 커지면 현재 data[i]가 tmp 로 들어가고
        # 전에 있던 tmp는 0 초기화 해주고 개수 1개 늘려준다.
        else:
            tmp = data[i]
            cnt += 1

    if cnt <= m:
        end = mid - 1
        result = min(result,mid)
    else:
        start = mid + 1
print(result)