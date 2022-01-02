n = int(input())
al = [int(a) for a in input().split()]
count = 0
while len([a for a in al if a % 2 != 0]) == 0:
    al = [a // 2 for a in al]
    count += 1
print(count)
