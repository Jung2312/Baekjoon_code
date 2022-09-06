n = int(input())

if(1 <= n <= 100):
    num = int(input())
    list = list(map(int, str(num)))
    sum = sum(list)
    
print(sum)