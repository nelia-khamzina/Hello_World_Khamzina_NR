not_count = input().split()
sum_n = 0

for i in not_count:
    if int(i) % 2 != 0:
        sum_n += int(i)
print(sum_n)