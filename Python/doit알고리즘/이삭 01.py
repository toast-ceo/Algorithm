import sys

input = sys.stdin.readline


def main(num, numbers):
    num = int(num)
    result = 0
    for i in range(num):
        result += int(numbers[i])

    return result


input_num = input()
input_numbers = input()

print(main(input_num, input_numbers))
