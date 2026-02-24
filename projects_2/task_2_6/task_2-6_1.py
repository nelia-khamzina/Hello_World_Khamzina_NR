pH = float(input("Введите значение pH: "))

if 0 <= pH < 7:
    print("Кислая среда")
elif pH == 7:
    print("Нейтральная среда")
elif 7 < pH <= 10:
    print("Щелочная среда")
else:
    print("Ошибочное pH")