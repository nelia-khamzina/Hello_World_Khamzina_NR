positivchik = input().split()
count_p = 0

for i in positivchik:
    if int(i) > 0:
        count_p += 1
print(count_p)