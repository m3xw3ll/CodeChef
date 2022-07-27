# https://www.codechef.com/submit/AGELIMIT
T = int(input())
for i in range(T):
    X, Y, A= [int(i) for i in input().split()]
    if A >= X and A < Y:
        print('YES')
    else:
        print('NO')