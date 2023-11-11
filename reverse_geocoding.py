import pandas as pd
import requests 
import json
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()
API_key = os.getenv("API_KEY")

df = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK7/assignment7_slim_hospital_coordinates.csv")

# combines string representations of 'X' and 'Y', separated by a comma.
df['GEO'] = df['X'].astype(str) + ',' + df['Y'].astype(str)
df_s = df.sample(100) #sample

google_response = [] #store result

for coord in df_s['GEO']: 

    reverse_geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='

# convert to url friendly 
    location_raw = coord
    location_clean = urllib.parse.quote(location_raw)

# form complete url
    url_request = reverse_geocode_url + location_clean + '&key=' + API_key
    response = requests.get(url_request)
    
# get json
    response_dictionary = response.json()
    address = response_dictionary['results'][0]['formatted_address']

# create dictionary named final
    final = {'address': address, 'coordinates': coord}
    google_response.append(final)

# print message that processing is completed
    print(f'....finished with {coord}')

# create df
df_add = pd.DataFrame(google_response)

# save df to csv file
df_add.to_csv('reverse_geocoding.csv')
