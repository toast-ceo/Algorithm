from sys import stdin

input = stdin.readline


def checkTime(times):
    available = []
    check = 9
    for time in times:
        start, end = time[0], time[1]
        if (check < start):
            available.append([check, start])
        check = end

    if (check != 18):
        available.append([check, 18])

    length = len(available)
    if (length == 0):
        print("Not available")
    else:
        print(length, "available:")
        for start, end in available:
            if (start == 9): start = "09"
            print(str(start) + "-" + str(end))


n, m = map(int, input().split())
reservations = dict()
for _ in range(n):
    room = input()
    reservations[room[:-1]] = []

for _ in range(m):
    room, start, tend = map(str, input().split())
    reservations[room].append([int(start), int(tend)])

last_check = False

# Key기준 정렬 순으로 체크
for room, times in sorted(reservations.items()):
    times.sort(key=lambda x: x[0])

    print("Room " + room + ":")
    checkTime(times)

    n -= 1  # 마지막 방은 구분선 안넣어줄 목적
    if (n != 0):
        print("-----")