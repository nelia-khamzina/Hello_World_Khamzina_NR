mass_protein = int(input('Введите массу белков: '))
mass_lipid = int(input('Введите массу жиров: '))
mass_carbohydrate = int(input('Введите массу углеводов: '))
print(f'Общая калорийность: {mass_protein * 4 + mass_lipid * 9 + mass_carbohydrate * 4} г.')