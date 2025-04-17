#ZMIANA TYPU DANYCH
import pandas as pd
import numpy as np

df = pd.read_csv('harddrive.csv', nrows= 3000)
print(df.head())

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d') #konwertacja na typ 'datetime'

df['year'] = df['date'].dt.year # dodanie kolumny year
print(df[['date', 'year']].head())

