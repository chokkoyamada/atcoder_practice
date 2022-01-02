n, y = map(int, input().split())

ans = [-1, -1, -1]
for man in range(n + 1):
    for gosen in range((n - man) + 1):
        sen = n - man - gosen
        if man * 10000 + gosen * 5000 + sen * 1000 == y:
            ans = [man, gosen, sen]
            break
print(" ".join([str(x) for x in ans]))
