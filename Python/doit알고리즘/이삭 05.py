import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

sum = 0
num_remainder = [0] * m

for i in range(n):
    sum += arr[i]
    num_remainder[sum % m] += 1

# 굳이 다른 수를 받지 않아도 되는 인덱스들을 더해줌
result = num_remainder[0]

# 계산
for i in num_remainder:
    result += i * (i - 1) // 2

print(result)