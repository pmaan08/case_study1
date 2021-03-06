#total population and urban population zip together stored in as a list of tuples
#data from ind_pop_data.csv 

import pandas as pd
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

df_urb_pop = next(urb_pop_reader)
print(df_urb_pop.head())

# Check out specific country
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list
pops_list = list(pops)

print(pops_list)
