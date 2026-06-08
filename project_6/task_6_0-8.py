import pandas as pd
df = pd.read_csv('wild_boars.csv')
for i in ['Male', 'Female']:
    with open("file_6_0-8_length_cabanchick.txt", "a") as file:
        std_len = df[df['gender'] == i]['length_cm'].std()
        mean_len = df[df['gender'] == i]['length_cm'].mean()
        cv_tusk_length_cm = (std_len / mean_len) * 100
        file.write(f"{i} coefficient of variation is {cv_tusk_length_cm:.2f} %")
        file.write(f"\n")
    file.close()