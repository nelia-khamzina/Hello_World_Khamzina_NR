with open("C:\\Users\\Compu\\Desktop\\khamzina_nr\\projects_2\\task_2_7\\task_2.txt", "r", encoding="utf-8") as file:
    dna = file.readlines()[1:]
dna_list = []
for seq in dna:
    for symbol in seq:
        if symbol != "\n":
            dna_list.append(symbol)
print("".join(dna_list))
print('')
for seq in dna:
    print(seq.replace("\n", ""))

print("Цикл выполнен")
file.close()