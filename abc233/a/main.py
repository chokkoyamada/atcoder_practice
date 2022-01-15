x, y = [int(x) for x in input().split()]

z = y - x
if z <= 0:
    print(0)
else:
    amari = z % 10
    if amari == 0:
        print((z) // 10)
    else:
        print((z + (10 - amari)) // 10)
