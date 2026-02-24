name = input("Введите ФИО: ")
f_name = f"ФИО исследователя : {name}{' ' * 10}"
date = input("Введите дату эксперимента: ")
f_date = f"Дата             : {date}"
name_ex = input("Введите название эксперимента: ").split()
f_name_ex = f"Эксперимент      : {' '.join(name_ex)}"
ex_cnclsn = input("Введите сделанный вывод: ").split()

# Часть кода, в котором высчитывается длина рамки таблицы в зависимости от длины введенного имени пользователя:))
with open("C:\\Users\\Compu\\Desktop\\khamzina_nr\\projects_2\\task_2_3\\journal.txt", "w", encoding="utf-8") as file:
    file.write(f"+-{'-' * len(f_name)}+\n")
    file.write(f"| Электронный лабораторный журнал{' ' * (len(f_name) - 31)}|\n")
    file.write(f"+-{'-' * len(f_name)}+\n")
    file.write(f"| {f_name}|\n")
    file.write(f"| {f_date}{' ' * (len(f_name) - len(f_date))}|\n")


    n_e_list = [name_ex[0]]
    # если эксперимент длиной меньше, чем строка с именем
    if len(f_name_ex) < len(f_name):
        file.write(f"| {f_name_ex}{' ' * (len(f_name) - len(f_name_ex))}\n")
    # если эксперимент большей длины
    else:
        file.write(f"| Эксперимент :{' ' * (len(f_name) - 13)}|\n")
        for i in range(1, len(name_ex)):
            if len(" ".join(n_e_list)) > len(f_name):
                file.write(f"| {' '.join(n_e_list[:-1])}{' ' * (len(f_name) - len(' '.join(n_e_list[:-1])))}|\n")
                n_e_list = [n_e_list[-1]]
            else:
                n_e_list.append(name_ex[i])


    file.write(f"+-{'-' * len(f_name)}+\n")


    # манипуляции с выводом
    e_c_list = [ex_cnclsn[0]]

    file.write(f"| Вывод :{' ' * (len(f_name) - 7)}|\n")
    for i in range(1, len(ex_cnclsn)):
        if len(" ".join(e_c_list)) > len(f_name):
            file.write(f"| {' '.join(e_c_list[:-1])}{' ' * (len(f_name) - len(' '.join(e_c_list[:-1])))}|\n")
            e_c_list = [e_c_list[-1]]
        else:
            e_c_list.append(ex_cnclsn[i])


    file.write(f"| {' '.join(e_c_list)}{' ' * (len(f_name) - len(' '.join(e_c_list)))}|\n")
    file.write(f"+-{'-' * len(f_name)}+\n")
file.close()