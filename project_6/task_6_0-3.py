import pandas as pd
df = pd.read_csv('wild_boars.csv')
column_names = df.columns.values
for i in column_names[2:]:
    median_param = df[i].median()
    with open("file_6_0-3_median_cabanchick.txt", "a") as file:
        file.write(f"Boars median {i} is {median_param:.2f}\n")
    file.close()
