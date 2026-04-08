list_index = input().split()
sum_l = 0
count_p = 0

for i in range(0, len(list_index)):
    if i % 2 == 0:
        sum_l += int(list_index[i])
        count_p += 1
        print(sum_l)
        print(count_p)
print(sum_l / count_p)