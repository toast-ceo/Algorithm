import sys
input = sys.stdin.readline


n = int(input())


def checkPrimeNum(check_number):
    # 에라토스테네스의 체로 소수인지 확인
    # 2부터 n의 제곱근까지의 모든 수를 확인함
    for i in range(2, int(check_number ** 0.5) + 1):
        # 나눠지면 소수 아님
        if int(check_number) % i == 0:
            return False
    return True


def dfs(num):
    # 목표 길이 도달 시 멈춤
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            # 10곱하고 i 더해서 자릿수 늘린 수가 소수일때만
            # dfs로 다음 자릿수 확인 넘김
            if checkPrimeNum(temp):
                dfs(temp)


# 맨마지막으로 맨 앞자리를 봤을 떄 소수여야하므로
# 일의자리숫자중에 소수로 시작을 한다.
dfs(2)
dfs(3)
dfs(5)
dfs(7)
