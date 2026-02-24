print('=== Анализ последовательности ДНК ===')
with open("C:\\Users\\Compu\\Desktop\\khamzina_nr\\projects_2\\task_2_5\\task_2.txt", "r", encoding="utf-8") as file:
    dna = file.readlines()[1:]
dna_list = []
for i in dna:
    for j in i:
        if j != "\n":
            dna_list.append(j)
dna = "".join(dna_list).upper()
lenght = len(dna)
print(f'Последовательность в верхнем регистре: {dna}')
print(f'Подсчёт нуклеотидов:')
print(f'A: {dna.count("A")} -> {round((dna.count("A") / lenght * 100), 1)}%')
print(f'T: {dna.count("T")} -> {round((dna.count("T") / lenght * 100), 1)}%')
print(f'G: {dna.count("G")} -> {round((dna.count("G") / lenght * 100), 1)}%')
print(f'C: {dna.count("C")} -> {round((dna.count("C") / lenght * 100), 1)}%')
print(f'Общая длина: {lenght} нуклеотидов')