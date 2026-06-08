import pandas as pd
df = pd.read_csv('wild_boars.csv')
column_names = df.columns.values
for i in column_names[2:]:
    mode_param = df[i].mode().values
    with open("file_6_0-4_mode_cabanchick.txt", "a") as file:
        file.write(f"Boars mode {i} is {mode_param}\n")
    file.close()
