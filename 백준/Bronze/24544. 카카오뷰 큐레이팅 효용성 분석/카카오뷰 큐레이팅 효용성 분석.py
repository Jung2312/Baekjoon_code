ctn_size = int(input())

like_list = list(map(int,input().split()))

dislike_list = list(map(int,input().split()))

like_sum = sum(like_list)
dis_sum = 0

for i in range(ctn_size):
    if dislike_list[i] == 0:
        dis_sum += like_list[i]

print(like_sum)
print(dis_sum)