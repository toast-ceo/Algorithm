import sys
input = sys.stdin.readline

# 문제는 버블 소트이지만 시간 초과 때문에 버블정렬로 풀 수 없다
# 따라서 N logN에 부합하는 병합 정렬을 사용해준다
# 20번의 로직에 swap을 해주는 카운트를 넣어준다
def merge_sort(start, end):
    global swap_count, A

    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        a, b = start, mid + 1
        temp = []

        while a <= mid and b <= end:
            if A[a] <= A[b]:
                temp.append(A[a])
                a += 1
            # 뒤에 있는 수가 앞으로 넘어올 때 카운팅
            else:
                temp.append(A[b])
                b += 1
                swap_count += (mid - a + 1)

        if a <= mid:
            temp = temp + A[a:mid + 1]
        if b <= end:
            temp = temp + A[b:end + 1]

        for i in range(len(temp)):
            A[start + i] = temp[i]


swap_count = 0
N = int(input())
print(N)

A = list(map(int, input().split()))
print(A)
merge_sort(0, N - 1)
print(swap_count)