name_new_reagent = input('Введите название нового реактива: ')
number_reagent = input('Введите количество реактива (целое число): ')
with open('C:\\Users\\Compu\\Desktop\\khamzina_nr\\projects_2\\task_2_2\\inventory.txt', 'w', encoding='utf-8') as file:
    file.write(f'Реактив {name_new_reagent} поступил на склад в количестве {number_reagent} шт.\n')
file.close()