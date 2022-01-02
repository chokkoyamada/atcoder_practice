n = int(input())
al = [int(a) for a in input().split()]
al = sorted(al, reverse=True)

alice = []
bob = []
while True:
    alice.append(al[0])
    al = al[1:]
    if len(al) == 0:
        break
    bob.append(al[0])
    al = al[1:]
    if len(al) == 0:
        break
print(sum(alice) - sum(bob))
