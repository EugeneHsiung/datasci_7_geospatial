import requests 
import urllib.parse
import json
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()
API = os.getenv("API_KEY")

df = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK7/assignment7_slim_hospital_addresses.csv")
df['GEO'] = df['ADDRESS'] + ' ' + df['CITY'] + ' ' + df['STATE']
df_s = df.sample(n=100) #sample

google_response = []

for address in df_s['GEO']: 

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + API
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address, 'lat': lat_response, 'lon': lng_response}
    google_response.append(final)

    print(f'....finished with {address}')

df_geo = pd.DataFrame(google_response)

df_geo.to_csv('geocoding.csv')

# Output shown in screenshots folder 