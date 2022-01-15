x = int(input())

ans_greater_5 = [
    123456,
    234567,
    345678,
    456789,
    654321,
    765432,
    876543,
    987654,
    1234567,
    2345678,
    3456789,
    7654321,
    8765432,
    9876543,
    12345678,
    23456789,
    87654321,
    98765432,
    123456789,
    987654321,
    9876543210,
]

len_x = len(str(x))
if len_x == 1 or len_x == 2:
    pass
elif len_x >= 6:
    x = min([i for i in ans_greater_5 if i >= x])

else:
    while True:
        len_x = len(str(x))
        lst = [int(i) for i in list(str(x))]
        lst_sabun = None
        for n in range(len_x - 1, 0, -1):
            sabun = lst[n] - lst[n - 1]
            if lst_sabun is None:
                lst_sabun = sabun
            elif lst_sabun != sabun:
                lst_sabun = -1
                break
        if lst_sabun > 0:
            break
        x = x + 1

print(x)
