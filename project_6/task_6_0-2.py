import pandas as pd
df = pd.read_csv('wild_boars.csv')
column_names = df.columns.values
for i in column_names[2:]:
    average_param = df[i].mean()
    with open("file_6_0-2_mean_cabanchick.txt", "a") as file:
        file.write(f"Boars average {i} is {average_param:.2f}\n")
    file.close()