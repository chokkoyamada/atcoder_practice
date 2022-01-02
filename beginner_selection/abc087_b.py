a = int(input())
b = int(input())
c = int(input())
x = int(input())

success = 0
for a1 in range(a + 1):
    for b1 in range(b + 1):
        for c1 in range(c + 1):
            if (500 * a1) + (100 * b1) + (50 * c1) == x:
                success += 1
print(success)
