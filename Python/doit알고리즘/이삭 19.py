import sys
input = sys.stdin.readline
import random

m, n = map(int, input().split())
arr = list(map(int, input().split()))


def QuickSelect(A, k):
    s, m, l = [], [], [];
    # quickselect에서 피봇을 설정할 때 0번째 요소가 아닌, random으로 설정하도록 하여 해결
    pivot = A[random.randint(0, len(A) - 1)]
    for i in A:
        if i < pivot:
            s.append(i)
        elif i == pivot:
            m.append(i)
        else:
            l.append(i)
    if len(s) >= k:
        return QuickSelect(s, k)
    elif len(s) + len(m) < k:
        return QuickSelect(l, k - len(s) - len(m))
    else:
        return pivot

print(QuickSelect(arr, n))
