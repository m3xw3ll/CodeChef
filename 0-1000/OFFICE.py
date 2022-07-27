# https://www.codechef.com/submit/OFFICE
T = int(input())
for i in range(T):
    X, Y = [int(i) for i in input().split()]
    print((4 * X) + Y)