# import sys
# input = sys.stdin.readline
#
# word = ('A', 'C', 'G', 'T')
#
# # L: DNA 문자열의 길이, P: 부분 문자열의 길이
# L, P = list(map(int, input().split()))
# # DNA: DNA 문자열
# DNA = input()
# # 부분 문자열의 포함되어야 할 A, C, G, T의 최소 개수
# N = dict(zip(word, map(int, input().split())))
#
#
# state = {w: 0 for w in word}
#
# def check():
#     for w in word:
#         if state[w] < N[w]: return False
#     return True
#
# R = 0
#
# for i in range(P):
#     state[DNA[i]] += 1
#
# if check(): R += 1
#
# for i in range(P, L):
#     state[DNA[i-P]] -= 1
#     state[DNA[i]] += 1
#     if check(): R += 1
#
# print(R)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = input()
a, c, g, t = map(int, input().split())
cnt = 0
dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# dic에 값 저장
for i in s[:m]:
    dic[i] += 1

# 답 체크
if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
    cnt += 1

# 슬라이싱 이동
for i in range(1, n - m + 1):
    dic[s[i-1]] -= 1
    dic[s[i-1+m]] += 1
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        cnt += 1
print(cnt)