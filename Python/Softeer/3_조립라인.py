import sys

n = int(sys.stdin.readline())
line = []
for i in range(n - 1):
    line.append(list(map(int, sys.stdin.readline().split())))

# 마지막 작업장 시간
finish = list(map(int, sys.stdin.readline().split()))
# 각 라인에서 총 걸리는 시간
time_a = 0
time_b = 0
# 각 작업장 라인중 이전 라인에서 걸린 시간
work_a = 0
work_b = 0

for i in range(n - 1):
    # n이 1일경우에는 작업장이 하나씩이기 때문에 둘중 제일 적은 시간인 경우에만 출력하면 된다.
    if n == 1:
        break

    # 오로지 a라인에서 작업한 시간과 b라인에서 작업하고 a라인으로 이동한 시간 비교
    time_a = min(line[i][0] + work_a, line[i][1] + line[i][3] + work_b)
    # 오로지 b라인에서 작업한 시간과 a라인에서 작업하고 b라인으로 이동한 시간 비교
    time_b = min(line[i][1] + work_b, line[i][0] + line[i][2] + work_a)
    # 각 라인에 최소 작업시간을 이전 라인에서 걸린 시간에 넣는다.
    work_a = time_a
    work_b = time_b

# 각각의 마지막 작업장 시간을 각 라인에서 총 걸린 시간에 더해준다.
time_a += finish[0]
time_b += finish[1]

# 각 라인에서 총 걸린 시간의 최소를 출력한다.
print(min(time_a, time_b))