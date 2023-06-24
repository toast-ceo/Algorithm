from sys import stdin
input = stdin.readline

a, b = map(int, input().split())
print('same') if a == b else print('A') if a > b else print('B')