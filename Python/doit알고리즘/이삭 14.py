import sys
import heapq
input = sys.stdin.readline

def solution(n):
    n = int(n)
    heap = []

    for i in range(n):
        temp = int(input())

        if temp != 0:
            heapq.heappush(heap, (abs(temp), temp)) # (우선 순위, 값)
        else:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)

num = input()
solution(num)