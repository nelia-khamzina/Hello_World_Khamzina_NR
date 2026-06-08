import pandas as pd
df = pd.read_csv('wild_boars.csv')
column_names = df.columns.values
for i in column_names[2:]:
    with open("file_6_0-2_per_cabanchick.txt", "a") as file:
        file.write(f"Percentile 25 (Q1):\t{df[i].quantile(0.25):.1f}\n")
        file.write(f"Median 50 (Q2):\t{df[i].quantile(0.50):.1f}\n")
        file.write(f"Percentile 75 (Q3):\t{df[i].quantile(0.75):.1f}\n")
        file.write(f"Percentile 90:\t{df[i].quantile(0.90):.1f}\n")
        file.write(f"Percentile 95:\t{df[i].quantile(0.95):.1f}\n")
        file.write(f"Max:\t{df[i].quantile(1.00):.1f}\n")
        file.write("\n")
    file.close()