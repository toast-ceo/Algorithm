from sys import stdin

input = stdin.readline

result = 0

for _ in range(5):
    start, end = input().split()
    start_hour, start_min = start.split(':')
    end_hour, end_min = end.split(':')

    hour = int(end_hour) - int(start_hour)
    minute = int(end_min) - int(start_min)

    result = result + (hour * 60) + minute

print(result)