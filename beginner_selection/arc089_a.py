n = int(input())
t = [0]
x = [0]
y = [0]
for n1 in range(n):
    _t, _x, _y = [int(n1) for n1 in input().split()]
    t.append(_t)
    x.append(_x)
    y.append(_y)

can = True
for i in range(len(t) - 1):
    dt = t[i + 1] - t[i]
    dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
    if dt < dist:
        can = False
    if dist % 2 != dt % 2:
        can = False
if can:
    print("Yes")
else:
    print("No")
