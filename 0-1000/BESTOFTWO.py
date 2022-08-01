# https://www.codechef.com/submit/BESTOFTWO
T = int(input())
for i in range(T):
    X, Y = [int(i) for i in input().split()]
    print(X) if X > Y else print(Y)