import math

n = int(input())
xy_list = []
for i in range(n):
    xy_list.append([int(xy) for xy in input().split()])

max_distance = 0

for a in xy_list:
    for b in xy_list:
        ans = round(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2), 8)
        if ans > max_distance:
            max_distance = ans

print(max_distance)

# B - Longest Segment

# 普通に全探索している。今回の問題ではそれで十分間に合う。
