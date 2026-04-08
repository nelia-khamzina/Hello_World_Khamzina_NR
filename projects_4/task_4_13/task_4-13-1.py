list_1 = input().split()

if int(list_1[0]) < int(list_1[1]):
    if int(list_1[0]) < int(list_1[2]):
        if int(list_1[0]) < int(list_1[3]):
            print(list_1[0])
        else:
            print(list_1[3])
    else:
        if int(list_1[2]) < int(list_1[3]):
            print(list_1[2])
        else:
            print(list_1[3])
else:
    if int(list_1[1]) < int(list_1[2]):
        if int(list_1[1]) < int(list_1[3]):
            print(list_1[1])
        else:
            print(list_1[3])
    else:
        if int(list_1[2]) < int(list_1[3]):
            print(list_1[2])
        else:
            print(list_1[3])