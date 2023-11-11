import requests 
import urllib.parse
import json
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()
API_key = os.getenv("API_KEY")

df = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK7/assignment7_slim_hospital_addresses.csv")

# combines string representations of 'X' and 'Y', separated by a comma.
df['GEO'] = df['ADDRESS'] + ' ' + df['CITY'] + ' ' + df['STATE']
df_s = df.sample(n=100) #sample

google_response = [] #store result

for address in df_s['GEO']: 

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

# convert to url friendly 
    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

# form complete url
    url_request_part1 = search + location_clean + '&key=' + API_key
    url_request_part1

# get json
    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

# create dictionary named final
    final = {'address': address, 'lat': lat_response, 'lon': lng_response}
    google_response.append(final)

# print message that processing is completed
    print(f'....finished with {address}')

# create df
df_geo = pd.DataFrame(google_response)

# save df to csv file
df_geo.to_csv('geocoding.csv')

# Output shown in screenshots folder 