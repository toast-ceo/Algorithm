
K, P, N = map(int, input().split())
# 수퍼바이러스에서는 아래코드를 활성화시켜줘야한다.
N *= 10

def pow(N):
    # 나머지계산도 분배법칙이 가능하다는 걸 활용하는게 첫번째
    mod = 1000000007
    if N <= 1:
        return (P ** N) % mod
    # N제곱은 (N/2)의 제곱과 같은걸 활용하는게 두번째. 시간복잡도 N -> log2N.
    if N % 2 == 0:
        return (pow(N//2) ** 2) % mod
    elif N % 2 == 1:
        return (P * pow(N//2) ** 2) % mod


print((K * pow(N)) % 1000000007)