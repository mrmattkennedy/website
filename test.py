import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv')
df['smoker'] = df['smoker'].replace({'yes': True, 'no': False})
df['charges'] = df['charges'].round(1)
total = df['charges'].sum()
temp = df.groupby('region')['charges'].sum() / total
print(temp)

#Show introductory info - we have x samples, here's what the first 5 look like.
#Next, explore