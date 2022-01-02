s = input()

ans = None
while True:
    if len(s) >= 6 and s[0:7] == "dreamer" and (len(s) == 7 or s[7] != "a"):
        s = s[7:]
    elif len(s) >= 6 and s[0:6] == "eraser":
        s = s[6:]
    elif len(s) >= 5 and s[0:5] == "dream":
        s = s[5:]
    elif len(s) >= 5 and s[0:5] == "erase":
        s = s[5:]
    elif len(s) == 0:
        ans = "YES"
        break
    else:
        ans = "NO"
        break
print(ans)
