name_substrate = input('Введите название питательной среды: ')
concentration = input('Введите концентрацию агара (%): ')
temperatur_sterelisation = input('Введите температуру стерилизации (°C): ')

with open("C:\\Users\\Compu\\Desktop\\khamzina_nr\\projects_2\\task_2_3\\recipe.txt", "w", encoding="utf-8") as file:
    file.write(f'\t{name_substrate.upper()}\n')
    file.write(f'Концентрация агара: {concentration}\n')
    file.write(f'Температура стерелизации: {temperatur_sterelisation}\n')
print(f'Файл "recipe.txt" успешно сформирован!')
file.close()