list_max = input().split()
num_max = int(list_max[0])

for i in list_max:
    if int(i) > num_max:
        num_max = int(i)
print(num_max)