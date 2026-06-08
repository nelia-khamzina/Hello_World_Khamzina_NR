import pandas as pd
df = pd.read_csv('wild_boars.csv')
for i in ['Male', 'Female']:
    with open("file_6_0-6_qar_cabanchick.txt", "a") as file:
        q1 = df[df['gender'] == i]['length_cm'].quantile(0.25)
        q3 = df[df['gender'] == i]['length_cm'].quantile(0.75)
        iqr = q3 - q1
        file.write(f"{i} Q1 (25%): {q1:.1f} kg\n")
        file.write(f"{i} Q3 (75%): {q3:.1f} kg\n")
        file.write(f"{i} IQR: {iqr:.1f} kg\n")
        file.write(f"\n")
    file.close()