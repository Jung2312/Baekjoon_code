bef = list(input())
aft = "".join(reversed(bef))
bef = "".join(bef)

if aft == bef:
    print(1)
else:
    print(0)
