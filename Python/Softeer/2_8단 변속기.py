import sys
sys = sys.stdin.readline

number_list = list(map(int, input().split())) # 숫자를 리스트화 시켜서 비교하기 쉽게 만듬

if number_list == [1,2,3,4,5,6,7,8]: # 1부터 오름차순이면
    print("ascending")

elif number_list == [8,7,6,5,4,3,2,1]: # 8부터 내림차순이면
    print("descending")

else: # 그 외
    print("mixed")



from sys import stdin
input = stdin.readline

arr = list(map(int, input().split()))

print('ascending') if arr == [1,2,3,4,5,6,7,8] else print('descending') if arr == [8,7,6,5,4,3,2,1] else print('mixed')


