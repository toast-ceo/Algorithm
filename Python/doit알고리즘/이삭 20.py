from sys import stdin
input = stdin.readline

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):  # i와 j가 가리키는 값 비교 -> 작은 값을 k에 넣기
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):  # 한쪽 리스트가 끝난 경우, 나머지 리스트를 넣어줌
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

R = merge_sort(arr)
for i in R:
    print(i)
