import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

df = pd.read_csv('https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv')
df['smoker'] = df['smoker'].replace({'yes': True, 'no': False})

charges_groupby = df.groupby('region')['charges'].mean()
print(charges_groupby)

children_groupby = df.groupby('children')['charges'].mean()
print(children_groupby)

smoker_groupby = df.groupby('smoker')['charges'].mean()
print(smoker_groupby)

sex_groupby = df.groupby('sex')['charges'].mean()
print(sex_groupby)

df['age_bins'] = pd.cut(df['age'], bins=8)
age_groupby = df.groupby('age_bins')['charges'].mean()
print(age_groupby)

df['bmi_bins'] = pd.cut(df['bmi'], bins=6)
bmi_groupby = df.groupby('bmi_bins')['charges'].mean()
print(bmi_groupby)


print(df.corr())
print(df.corr(method='kendall'))
print(df.corr(method='spearman'))