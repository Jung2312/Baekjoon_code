while(True):
    su = int(input())

    N = list(map(int,input().split()))

    if N.count(1) <= 0:
        acksu = max(N) * min(N)
        break
    else:
        continue
    
print(acksu)