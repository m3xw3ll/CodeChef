# https://www.codechef.com/submit/INSURANCE
n = int(input())
for i in range(n):
    X, Y = [int(i) for i in input().split()]
    if Y > X:
        print(X)
    else:
        print(Y)