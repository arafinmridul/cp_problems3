# 0  8 12 15 20
# 0  1 2  3  8 l2r cost
# 14 6 2  1  0 r2l cost

import sys

def solve() :
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    l2r = [0] * n
    for i in range(n-1):
        if i==0 or a[i]-a[i-1] > a[i+1]-a[i]:
            l2r[i+1] = l2r[i] + 1
        else:
            l2r[i+1] = l2r[i]+a[i+1]-a[i]

    r2l = [0] * n
    for i in range(n-1, 0, -1):
        if i==n-1 or a[i+1]-a[i] > a[i]-a[i-1]:
            r2l[i-1] = r2l[i] + 1
        else:
            r2l[i-1] = r2l[i]+a[i]-a[i-1]

    q = int(input())
    for _ in range(q):
        l, r = map(int, sys.stdin.readline().split())
        l -= 1
        r -= 1
        if l < r :
            sys.stdout.write(str(l2r[r]-l2r[l]) + '\n')
        else:
            sys.stdout.write(str(r2l[r]-r2l[l]) + '\n')

t = int(sys.stdin.readline())
for _ in range(t) :
    solve()
