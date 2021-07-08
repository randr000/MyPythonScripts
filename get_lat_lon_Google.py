#Gets the longitude and latittude for an address using the Google Maps API

import json
import time
import pandas as pd
import urllib.error
import urllib.parse
import urllib.request

#Gets api key from txt file
with open(r".txt","r") as file:
    API_KEY = r"&key=" + file.readline()
# print(api_key)
GEO_URL = r"https://maps.googleapis.com/maps/api/geocode/json?&address="

#Gets df of all addresses
df = pd.read_csv(r".csv")
# df = pd.read_csv(r"-test.csv")

#Removes duplicate addresses
unique_search_address = df['SearchAddress'].unique()

headers = ['SearchAddress','LAT','LON']
lat_lon = []
row = 1

for addr in unique_search_address:
    f_addr = addr.replace(",", "").replace(" ", "%20")
    url = GEO_URL + f_addr + API_KEY
    
    try:
        result = json.load(urllib.request.urlopen(url))
        lat_lon.append((
                        addr,
                        result['results'][0]['geometry']['location']['lat'],
                        result['results'][0]['geometry']['location']['lng']))

    except:
        lat_lon.append((addr, None, None))

    #Lets user know what row is being searched and prints to console, helpful in knowing script is running successfully but otherwise not necessary
    print(row)
    row = row + 1

df_join = pd.DataFrame(lat_lon, columns=headers)

df = df.merge(df_join, how='left', on='SearchAddress')

df.to_csv(r".csv", index=False)
# df.to_csv(r"test-results.csv", index=False)