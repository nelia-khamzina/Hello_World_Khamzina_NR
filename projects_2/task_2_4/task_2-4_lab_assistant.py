volume = int(input('Введите нужный объем раствора (в мл): '))
with open("C:\\Users\\Compu\\Desktop\\khamzina_nr\\projects_2\\task_2_4\\reciepe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write(f"{'-' * 23}\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли:  {(volume * 0.009):.2f} г\n")
    file.write("Объем воды:  [V] мл\n")
file.close()