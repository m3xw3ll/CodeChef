# https://www.codechef.com/submit/DETSCORE
T = int(input())
for i in range(T):
    X, N = [int(i) for i in input().split()]
    print(X // 10 * N)
