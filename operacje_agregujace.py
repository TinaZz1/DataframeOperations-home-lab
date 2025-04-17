# OPERACJE AGREGUJĄCE
import pandas as pd
import numpy as np

df = pd.read_csv('realtor_data.csv')

properties_information = df[['status', 'price', 'state', 'zip_code', 'house_size']]
print(properties_information.head())

pd.options.display.float_format = '{:,.0f}'.format #konwersja z float na int
max_price = df.groupby('state')['price'].max()
print(max_price)

available_properties = df[df['status'] == 'for_sale'].groupby('zip_code').size()
print(available_properties)