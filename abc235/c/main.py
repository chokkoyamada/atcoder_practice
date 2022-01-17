n, q = [int(x) for x in input().split()]
al = [int(x) for x in input().split()]

xkl = []
for i in range(q):
    inputted = input().split()
    xkl.append(tuple([int(x) for x in inputted]))

appear = {}

for i in range(n):
    a = al[i]
    if a in appear:
        appear[a].append(i)
    else:
        appear[a] = [i]

for xk in xkl:
    x = xk[0]
    k = xk[1]
    if x in appear:
        if len(appear[x]) >= k:
            print(appear[x][k - 1] + 1)
        else:
            print(-1)
    else:
        print(-1)
