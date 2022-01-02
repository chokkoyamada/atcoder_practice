n, a, b = map(int, input().split())

total_sum = 0
for n1 in range(n + 1):
    sum1 = sum([int(x) for x in list(str(n1))])
    if (a <= sum1) and (sum1 <= b):
        total_sum += n1
print(total_sum)
