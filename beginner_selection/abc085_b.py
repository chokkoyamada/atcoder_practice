n = int(input())
dl = []
for x in range(n):
    dl.append(int(input()))

unique_dl = list(set(dl))
print(len(unique_dl))
