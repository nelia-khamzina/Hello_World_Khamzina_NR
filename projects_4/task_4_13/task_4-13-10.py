list_index = input().split()
sum_l = 0

for i in range(0, len(list_index)):
    if i % 2 != 0:
        sum_l += int(list_index[i])
print(sum_l)