A = int(input())
B = int(input())
C = int(input())

gop = A * B * C

gop_list = list(map(int,str(gop)))

print(gop_list.count(0))

for i in range(1, 10):
    print(gop_list.count(i))