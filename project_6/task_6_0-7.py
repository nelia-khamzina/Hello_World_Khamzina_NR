import pandas as pd
df = pd.read_csv('wild_boars.csv')
column_names = df.columns.values
for i in column_names[2:]:
    with open("file_6_0-7_something_cabanchick.txt", "a") as file:
        variance_all = df[i].var()
        file.write(f"{i} variance is {variance_all:.2f}\n")
        std_all = df[i].std()
        file.write(f"{i} standart deviation is {std_all:.2f}\n")
        cv_all = (df[i].std() / df[i].mean()) * 100
        file.write(f"{i} coefficient of variation is {cv_all:.2f} %\n")
        file.write("\n")
    file.close()