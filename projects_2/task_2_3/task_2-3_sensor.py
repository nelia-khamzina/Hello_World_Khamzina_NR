name_operator = input('Введите название питательной среды: ')
current_pressure = input('Введите текущее значение давления (Па): ')

with open("C:\\Users\\Compu\\Desktop\\khamzina_nr\\projects_2\\task_2_3\\sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f'{name_operator}\t{current_pressure}')
print(f'Данные успешно сохранены в sensor_log.txt')
file.close()