n = int(input())
hl = [int(x) for x in input().split()]

x1 = hl.pop(0)
ans = None
for i in range(n):
    if len(hl) == 0:
        ans = x1
        break
    x2 = hl.pop(0)
    if x1 >= x2:
        ans = x1
        break
    x1 = x2

print(ans)
