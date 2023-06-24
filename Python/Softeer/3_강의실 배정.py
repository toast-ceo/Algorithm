import sys
import heapq

N = int(sys.stdin.readline())
meeting_time = []

for _ in range(N):
    start, end = list(map(int, sys.stdin.readline().split()))
    # 끝나는 시간이 가장 작은 것을 맨 앞에 넣어준다, 만약 시작 시간이 같을 때에는 가장 작은 시간부터 오름차순으로
    heapq.heappush(meeting_time, (end, start))

end_time = 0
cnt = 0

while meeting_time:
    if meeting_time[0][1] >= end_time:
        end_time = heapq.heappop(meeting_time)[0]
        cnt += 1
        continue

    heapq.heappop(meeting_time)

print(cnt)