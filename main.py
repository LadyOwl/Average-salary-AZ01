import pandas as pd

df = pd.read_csv('dz.csv')

df.fillna(0, inplace=True)

average_salary_by_city = df.groupby('City')['Salary'].mean()

print(average_salary_by_city)