# https://www.codechef.com/submit/TALLER
T = int(input())
for i in range(T):
    X, Y = [int(i) for i in input().split()]
    print("A") if X > Y else print("B")