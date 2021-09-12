xy=list()

N=int(input())

for i in range(N):
    a, b=map(int, input().split())
    xy.append([a, b])

xy.sort()

for i in range(N):
    print(xy[i]);