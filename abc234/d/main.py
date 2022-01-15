n, k = [int(i) for i in input().split()]
pl = [int(i) for i in input().split()]

pl_index = []
for j in range(len(pl)):
    pl_index.append((j, pl[j]))

pl_index.sort(key=lambda x: x[1], reverse=True)

for i in range(k, n + 1):
    x = [y[1] for y in pl_index if y[0] < i]
    print(x[k - 1])

# D - Prefix K-th Max

# 問題に挙げられていたテストケースは通せたが、実行時間オーバー。
