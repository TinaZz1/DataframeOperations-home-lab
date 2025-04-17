#GRUPOWANIE DANYCH
import pandas as pd
import numpy as np

df = pd.read_csv('realtor_data.csv')
print(df)

pd.options.display.float_format = '{:,.0f}'.format
acres_in_cities = df.groupby('city').agg({'acre_lot':['sum']})
print(acres_in_cities)

avg_property_price = df.groupby('city')['price'].mean()
print(avg_property_price)



df_properties = pd.read_csv('realtor_data.csv')

