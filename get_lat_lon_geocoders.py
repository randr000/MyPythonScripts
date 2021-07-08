#Get longitude and latitude using geocoders API

from geopy.geocoders import Nominatim
import pandas as pd
import time
import csv

# df = pd.read_csv(r".csv")
df = pd.read_csv(r"test.csv")
unique_search_address = df['SearchAddress'].unique()
# print(len(unique_search_address))
headers = ['SearchAddress','LAT','LON']
lat_lon = []

locator = Nominatim(user_agent="myGeocoder")

row = 1

for addr in unique_search_address:
    try:
        location = locator.geocode(addr)
        lat_lon.append((addr, location.latitude, location.longitude))
    except:
        lat_lon.append((addr, None, None))
    print(row)
    row = row + 1

    #Free API and not allowed to make too many calls at one time, this creates a slight delay between each
    time.sleep(1)

df_join= pd.DataFrame(lat_lon, columns=headers)

df = df.merge(df_join, how='left', on='SearchAddress')

df.to_csv(r"results.csv")
# df.to_csv(r"test-results.csv")