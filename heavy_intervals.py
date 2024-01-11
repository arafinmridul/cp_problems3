# CF 1909C

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort()
    b.sort()
    c.sort()

    s = t = r = 0
    j = 0
    d = [0] * n
    e = [0] * n

    for i in range(n):
        while j < n and b[j] < a[i]:
            d[t] = b[j] - e[r - 1]
            t += 1
            j += 1
            r -= 1
        e[r] = a[i]
        r += 1

    while j < n:
        d[t] = b[j] - e[r - 1]
        t += 1
        j += 1
        r -= 1

    d.sort()

    for i in range(n):
        s += d[i] * c[n - i - 1]

    print(s)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
