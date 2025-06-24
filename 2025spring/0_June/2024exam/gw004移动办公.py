t, m = map(int, input().split())
p, n = [], []
for i in range(t):
    x, y = map(int, input().split())
    p.append(x)
    n.append(y)
mp, mn = [0] * t, [0] * t
mp[0], mn[0] = p[0], n[0]
for i in range(1, t):
    mp[i] = max(mp[i - 1], mn[i - 1] - m) + p[i]
    mn[i] = max(mn[i - 1], mp[i - 1] - m) + n[i]
print(max(mp[t-1],mn[t-1]))
