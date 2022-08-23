def name_in():
    while True:
        na = input()
        if 'a' <= na <= 'z' and len(na) <= 20:
            return str(na)
        else:
            break


name = set()
noname = set()
n, m = map(int,input().split())
if n <= 500000 and m <= 500000:
    for i in range(m):
        na = name_in()
        name.add(na)

    for j in range(n):
        na = name_in()
        noname.add(na)

    name = noname.intersection(name)
    print(len(name))

    for k in sorted(name):
        print(k)