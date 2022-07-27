# https://www.codechef.com/submit/FAIRPASS
T = int(input())
for i in range(T):
    X, Y = [int(i) for i in input().split()]
    if X < Y:
        print("YES")
    else:
        print("NO")