# https://www.codechef.com/submit/BURGERS
T = int(input())
for i in range(T):
    A, B = [int(i) for i in input().split()]
    if A < B:
        print(A)
    else:
        print(B)