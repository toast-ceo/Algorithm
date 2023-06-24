import sys
input = sys.stdin.readline

n, m = map(int, input().split())
limit_info =[0]*101

now = 1

for _ in range(n):
    section, speed = map(int, input().split())
    for i in range(now, now+section):
        limit_info[i] = speed

    now = now+section

result = 0
now = 1
for _ in range(m):
    section, speed = map(int,input().split())
    for i in range(now, now+section):
        result = max(result, speed-limit_info[i])
    now = now+section

print(result)